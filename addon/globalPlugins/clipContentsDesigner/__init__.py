# -*- coding: UTF-8 -*-
# clipContentsDesigner: a global plugin for managing clipboard text
#Copyright (C) 2012-2019 Noelia Ruiz Martínez, other contributors
# Released under GPL 2

import addonHandler
import globalPluginHandler
import api
import textInfos
import ui
import win32clipboard
import treeInterceptorHandler
import config
import core
import wx
import gui
from gui import SettingsPanel, NVDASettingsDialog, guiHelper
from keyboardHandler import KeyboardInputGesture
from globalCommands import SCRCAT_TEXTREVIEW, SCRCAT_CONFIG

addonHandler.initTranslation()

ADDON_SUMMARY = addonHandler.getCodeAddon().manifest["summary"]
try:
	ADDON_PANEL_TITLE = unicode(ADDON_SUMMARY)
except NameError:
	ADDON_PANEL_TITLE = str(ADDON_SUMMARY)
	
confspec = {
	"separator": "string(default="")",
	"addTextBefore": "boolean(default=False)",
	"confirmToAdd": "boolean(default=False)",
	"confirmToClear": "boolean(default=False)",
	"confirmToCopy": "boolean(default=False)",
	"confirmToCut": "boolean(default=False)",
	"confirmationRequirement": "integer(default=0)",
	"browseableTextFormat": "integer(default=0)",
	"maxLengthForBrowseableText": "integer(default=100000)",
}
config.conf.spec["clipContentsDesigner"] = confspec

### Constants

BROWSEABLETEXT_FORMATS = [
			# Translators: label of a dialog.
			_("Preformatted text in HTML"),
			# Translators: label of a dialog.
			_("HTML as shown in a web browser"),
			# Translators: label of a dialog.
			_("Raw text"),
		]

def getBookmark():
	try:
		separator = config.conf["clipContentsDesigner"]["separator"]
	except KeyError:
		separator = None
	if not separator:
		bookmark = "\r\n"
	else:
		bookmark = "\r\n%s\r\n" % separator
	return bookmark

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	scriptCategory = SCRCAT_TEXTREVIEW

	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		NVDASettingsDialog.categoryClasses.append(AddonSettingsPanel)

		self._copyStartMarker = None

	def terminate(self):
		NVDASettingsDialog.categoryClasses.remove(AddonSettingsPanel)

	def onSettings(self, evt):
		gui.mainFrame._popupSettingsDialog(NVDASettingsDialog, AddonSettingsPanel)

	def script_settings(self, gesture):
		wx.CallAfter(self.onSettings, None)
	script_settings.category = SCRCAT_CONFIG
	# Translators: message presented in input mode.
	script_settings.__doc__ = _("Shows the Clip Contents Designer settings.")

	def clearClipboard(self):
		try:
			win32clipboard.OpenClipboard()
			win32clipboard.EmptyClipboard()
			# Translators: message presented when the clipboard content has been deleted.
			ui.message(_("Clipboard cleared"))
		except win32clipboard.error:
			# Translators: message presented when the clipboard content cannot be deleted.
			ui.message(_("Clipboard not cleared"))
		finally:
			win32clipboard.CloseClipboard()

	def getSelectedText(self):
		obj=api.getFocusObject()
		treeInterceptor=obj.treeInterceptor
		if hasattr(treeInterceptor,'TextInfo') and not treeInterceptor.passThrough:
			obj=treeInterceptor
		try:
			info=obj.makeTextInfo(textInfos.POSITION_SELECTION)
		except (RuntimeError, NotImplementedError):
			info=None
		if not info or info.isCollapsed:
			return None
		return info.clipboardText

	def getMath(self):
		try:
			obj = api.getNavigatorObject()
			mathMl = obj.mathMl
		except (AttributeError, NotImplementedError, LookupError):
			return None
		try:
			import mathPres
		except ImportError:
			return None
		mathPres.ensureInit()
		if mathPres.brailleProvider:
			text = mathPres.brailleProvider.getBrailleForMathMl(mathMl)
			return text

	def script_setSelectionStartMarker(self, gesture):
		self._copyStartMarker = api.getReviewPosition().copy()
		# Translators: message presented when the start marker for appending text has been set using the review cursor.
		ui.message(_("Start marker set"))
	# Translators: message presented in input mode.
	script_setSelectionStartMarker.__doc__ = _("Marks the current position of the review cursor as the start of text to be appended to the clipboard.")

	def getTextToAdd(self):
		newText = self.getSelectedText() or self.getMath()
		if not newText:
			if not self._copyStartMarker:
				# Translators: message presented when it's not possible to add text, since no text has been selected or marked.
				ui.message(_("No selection. No start marker set"))
				return
			pos = api.getReviewPosition().copy()
			if self._copyStartMarker.obj != pos.obj:
				# Translators: Message presented when a start marked has been placed, but not in the current object.
				ui.message(_("The start marker must reside within the same object"))
				return
			pos.move(textInfos.UNIT_CHARACTER, 1, endPoint="end")
			pos.setEndPoint(self._copyStartMarker, "startToStart")
			if not pos.compareEndPoints(pos, "startToEnd") < 0:
				# Translators: message presented when review cursor has been used to add text and there is no text to add.
				ui.message(_("No text to add"))
				return
			newText = pos.clipboardText
			self._copyStartMarker = None
		try:
			clipData = api.getClipData()
			if config.conf["clipContentsDesigner"]["addTextBefore"]:
				text = newText+getBookmark()+clipData
			else:
				text = clipData+getBookmark()+newText
		except TypeError:
			text = newText
		return text

	def requiredFormatInClip(self):
		if config.conf["clipContentsDesigner"]["confirmationRequirement"] == 0:
			return True
		if config.conf["clipContentsDesigner"]["confirmationRequirement"] == 1:
			try:
				clipData = api.getClipData()
				return True
			except TypeError:
				return False
		win32clipboard.OpenClipboard()
		clipFormat = win32clipboard.EnumClipboardFormats()
		win32clipboard.CloseClipboard()
		if clipFormat:
			return True
		return False

	def confirmAdd(self):
		text = self.getTextToAdd()
		if not text:
			return
		# Translators: Label of a dialog.
		if gui.messageBox(_("Please, confirm if you want to add text to the clipboard"),
			# Translators: Title of a dialog.
			_("Adding text to clipboard"), wx.OK|wx.CANCEL) == wx.OK:
				if api.copyToClip(text):
					# Translators: message presented when the text has been added to the clipboard.
					core.callLater(200, ui.message, _("Added"))
				else:
					# Translators: message presented when the text cannot be added to the clipboard.
					core.callLater(200, ui.message, _("Cannot add"))

	def performAdd(self):
		text = self.getTextToAdd()
		if api.copyToClip(text):
			# Translators: message presented when the text has been added to the clipboard.
			ui.message(_("Added"))
		else:
			# Translators: message presented when the text cannot be added to the clipboard.
			ui.message(_("Cannot add"))

	def script_add(self, gesture):
		if (config.conf["clipContentsDesigner"]["confirmToAdd"] and not gui.isInMessageBox
			and self.requiredFormatInClip()):
				wx.CallAfter(self.confirmAdd)
		else:
			self.performAdd()
	# Translators: message presented in input mode.
	script_add.__doc__ = _("Retrieves the selected string or the text from the previously set start marker up to and including the current position of the review cursor, and adds it to the clipboard.")

	def confirmClear(self):
		# Translators: Label of a dialog.
		if gui.messageBox(_("Please, confirm if you want to clear the clipboard"),
			# Translators: Title of a dialog.
			_("Clearing clipboard"), wx.OK|wx.CANCEL) != wx.OK:
				return
		try:
			win32clipboard.OpenClipboard()
			win32clipboard.EmptyClipboard()
			# Translators: message presented when the clipboard content has been deleted.
			core.callLater(200, ui.message, _("Clipboard cleared"))
		except win32clipboard.error:
			# Translators: message presented when the clipboard content cannot be deleted.
			core.callLater(200, ui.message, _("Clipboard not cleared"))
		finally:
			win32clipboard.CloseClipboard()

	def script_clear(self, gesture):
		if (config.conf["clipContentsDesigner"]["confirmToClear"] and not gui.isInMessageBox
			and self.requiredFormatInClip()):
			wx.CallAfter(self.confirmClear)
		else:
			self.clearClipboard()
	# Translators: message presented in input mode.
	script_clear.__doc__ = _("Deletes the added text and the content of the clipboard.")

	def copy(self):
		obj=api.getFocusObject()
		treeInterceptor=obj.treeInterceptor
		if isinstance(treeInterceptor,treeInterceptorHandler.DocumentTreeInterceptor) and not treeInterceptor.passThrough:
			treeInterceptor.script_copyToClipboard(None)
		else:
			KeyboardInputGesture.fromName("control+c").send()

	def confirmCopy(self):
		text = self.getSelectedText()
		# Translators: Label of a dialog.
		if gui.messageBox(_("Please, confirm if you want to copy to the clipboard"),
			# Translators: Title of a dialog.
			_("Copying to clipboard"), wx.OK|wx.CANCEL) != wx.OK:
				return
		if text:
			api.copyToClip(text)
		else:
			core.callLater(200, self.copy)

	def script_copy(self, gesture):
		if (config.conf["clipContentsDesigner"]["confirmToCopy"] and not gui.isInMessageBox
			and self.requiredFormatInClip()):
				wx.CallAfter(self.confirmCopy)
		else:
			self.copy()
	# Translators: message presented in input mode.
	script_copy.__doc__ = _("Copies to the clipboard, with the possibility of being asked for a previous confirmation")

	def cut(self):
		KeyboardInputGesture.fromName("control+x").send()

	def confirmCut(self):
		# Translators: Label of a dialog.
		if gui.messageBox(_("Please, confirm if you want to cut from the clipboard"),
			# Translators: Title of a dialog.
			_("Cutting from clipboard"), wx.OK|wx.CANCEL) != wx.OK:
				return
		core.callLater(200, self.cut)

	def script_cut(self, gesture):
		if (config.conf["clipContentsDesigner"]["confirmToCut"] and not gui.isInMessageBox
			and self.requiredFormatInClip()):
				wx.CallAfter(self.confirmCut)
		else:
			self.cut()
	# Translators: message presented in input mode.
	script_cut.__doc__ = _("Cuts from the clipboard, with the possibility of being asked for a previous confirmation")

	def script_showClipboardText(self, gesture):
		try:
			text = api.getClipData()
		except:
			text = None
		if not text or not isinstance(text,basestring) or text.isspace():
			win32clipboard.OpenClipboard()
			clipFormat = win32clipboard.EnumClipboardFormats()
			win32clipboard.CloseClipboard()
			if clipFormat:
				# Translators: presented when clipboard is not empty, but there is no text to show in browse mode.
				ui.message(_("Clipboard is not empty, but there is no text to show"))
			else:
				# Translators: presented when clipboard is empty.
				ui.message(_("Clipboard is empty"))
		else:
			maxLength = config.conf["clipContentsDesigner"]["maxLengthForBrowseableText"] if config.conf["clipContentsDesigner"]["maxLengthForBrowseableText"] <= len(text) else len(text)
			format = config.conf["clipContentsDesigner"]["browseableTextFormat"]
			html = True
			if format == 0:
				browseableText = "<pre>%s</pre>" % text.strip()[:maxLength]
			elif format == 1:
				browseableText = text.strip()[:maxLength]
			else:
				browseableText = text[:maxLength]
				html = False
			# Translators: title of a browseable message.
			ui.browseableMessage(browseableText, _("Clipboard text ({max}/{current} - {formatForTitle})".format(max=maxLength, current=len(text), formatForTitle=BROWSEABLETEXT_FORMATS[format])), html)
	script_showClipboardText.__doc__ = _("Shows the clipboard text in browse mode")

	__gestures = {
		"kb:NVDA+windows+c": "add",
		"kb:NVDA+windows+x": "clear",
		"kb:NVDA+windows+f9": "setSelectionStartMarker",
	}

class AddonSettingsPanel(SettingsPanel):

	title = ADDON_PANEL_TITLE

	def makeSettings(self, settingsSizer):
		sHelper = guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		# Translators: label of a dialog.
		setSeparatorLabel = _("Type the string to be used as a &separator between contents added to the clipboard.")
		setSeparatorLabeledCtrl = gui.guiHelper.LabeledControlHelper(self, setSeparatorLabel, wx.TextCtrl)
		self.setSeparatorEdit = setSeparatorLabeledCtrl.control
		try:
			self.setSeparatorEdit.SetValue(config.conf["clipContentsDesigner"]["separator"])
		except KeyError:
			pass
		# Translators: label of a dialog.
		self.addTextBeforeCheckBox = sHelper.addItem(wx.CheckBox(self, label= _("&Add text before clip data")))
		self.addTextBeforeCheckBox.SetValue(config.conf["clipContentsDesigner"]["addTextBefore"])
		# Translators: label of a dialog.
		confirmBoxLabel = _("Sele&ct the actions which require previous confirmation")
		confirmChoices = [
			# Translators: label of a dialog.
			_("Confirm to add text"),
			# Translators: label of a dialog.
			_("Confirm to clear clipboard"),
			# Translators: label of a dialog.
			_("Confirm to emulate copy"),
			# Translators: label of a dialog.
			_("Confirm to emulate cut"),
		]
		self.confirmList=sHelper.addLabeledControl(confirmBoxLabel, gui.nvdaControls.CustomCheckListBox, choices=confirmChoices)
		checkedItems = []
		if config.conf["clipContentsDesigner"]["confirmToAdd"]:
			checkedItems.append(0)
		if config.conf["clipContentsDesigner"]["confirmToClear"]:
			checkedItems.append(1)
		if config.conf["clipContentsDesigner"]["confirmToCopy"]:
			checkedItems.append(2)
		if config.conf["clipContentsDesigner"]["confirmToCut"]:
			checkedItems.append(3)
		self.confirmList.CheckedItems = checkedItems
		self.confirmList.Select(0)
		# Translators: label of a dialog.
		confirmRequirementsLabel = _("&Request confirmation before performing the selected actions when:")
		requirementChoices = [
			# Translators: label of a dialog.
			_("Always"),
			# Translators: label of a dialog.
			_("If the clipboard contains text"),
			# Translators: label of a dialog.
			_("If the clipboard is not empty"),
		]
		self.confirmRequirementChoices = sHelper.addLabeledControl(confirmRequirementsLabel, wx.Choice, choices=requirementChoices)
		self.confirmRequirementChoices.SetSelection(config.conf["clipContentsDesigner"]["confirmationRequirement"])
		# Translators: label of a dialog.
		formatLabel = _("&Format to show the clipboard text in browse mode:")
		self.formatChoices = sHelper.addLabeledControl(formatLabel, wx.Choice, choices=BROWSEABLETEXT_FORMATS)
		self.formatChoices.SetSelection(config.conf["clipContentsDesigner"]["browseableTextFormat"])
		# Translators: label of a dialog.
		maxLengthLabel=wx.StaticText(self,-1,label=_("&Maximum number of characters when showing clipboard text in browse mode"))
		self.maxLengthEdit=gui.nvdaControls.SelectOnFocusSpinCtrl(self, min=1, max=1000000, initial=config.conf["clipContentsDesigner"]["maxLengthForBrowseableText"])

	def postInit(self):
		self.setSeparatorEdit.SetFocus()

	def onSave(self):
		config.conf["clipContentsDesigner"]["separator"] = self.setSeparatorEdit.GetValue()
		config.conf["clipContentsDesigner"]["addTextBefore"] = self.addTextBeforeCheckBox.GetValue()
		config.conf["clipContentsDesigner"]["confirmToAdd"] = self.confirmList.IsChecked(0)
		config.conf["clipContentsDesigner"]["confirmToClear"] = self.confirmList.IsChecked(1)
		config.conf["clipContentsDesigner"]["confirmToCopy"] = self.confirmList.IsChecked(2)
		config.conf["clipContentsDesigner"]["confirmToCut"] = self.confirmList.IsChecked(3)
		config.conf["clipContentsDesigner"]["confirmationRequirement"] = self.confirmRequirementChoices.GetSelection()
		config.conf["clipContentsDesigner"]["browseableTextFormat"] = self.formatChoices.GetSelection()
		config.conf["clipContentsDesigner"]["maxLengthForBrowseableText"] = self.maxLengthEdit.GetValue()
