# -*- coding: UTF-8 -*-
# clipContentsDesigner: a global plugin for managing clipboard text
#Copyright (C) 2012-2016 Noelia Ruiz Martínez, other contributors
# Released under GPL 2

import addonHandler
import globalPluginHandler
import api
import textInfos
import ui
import msg # Developed by Alberto Buffolino
import win32clipboard
import config
import wx
import gui
from gui import SettingsDialog, guiHelper
from globalCommands import SCRCAT_TEXTREVIEW, SCRCAT_CONFIG

addonHandler.initTranslation()

confspec = {
	"separator": "string(default="")",
	"addTextBefore": "boolean(default=False)",
	"confirmToAdd": "boolean(default=False)",
	"confirmToClean": "boolean(default=False)",
	"confirmToCopy": "boolean(default=False)",
}
config.conf.spec["clipContentsDesigner"] = confspec

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
		self.prefsMenu = gui.mainFrame.sysTrayIcon.preferencesMenu
		self.settingsItem = self.prefsMenu.Append(wx.ID_ANY,
			# Translators: name of the option in the menu.
			_("&Clip Contents Designer settings..."),
			"")
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onSettings, self.settingsItem)

		self._copyStartMarker = None

	def terminate(self):
		try:
			self.prefsMenu.RemoveItem(self.settingsItem)
		except wx.PyDeadObjectError:
			pass

	def onSettings(self, evt):
		gui.mainFrame._popupSettingsDialog(AddonSettingsDialog)

	def script_settings(self, gesture):
		wx.CallAfter(self.onSettings, None)
	script_settings.category = SCRCAT_CONFIG
	# Translators: message presented in input mode.
	script_settings.__doc__ = _("Shows the Clip Contents Designer settings dialog.")

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
				msg.message("The start marker must reside within the same object")
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

	def confirmAdd(self):
		text = self.getTextToAdd()
		if not text:
			return
		# Translators: Label of a dialog.
		if gui.messageBox(_("Please, confirm if you want to add text to the clipboard"),
			# Translators: Title of a dialog.
			_("Adding text to clipboard"), wx.OK|wx.CANCEL) == wx.OK:
				api.copyToClip(text)

	def performAdd(self):
		text = self.getTextToAdd()
		if api.copyToClip(text):
			# Translators: message presented when the text has been added to the clipboard.
			ui.message(_("Added"))
		else:
			# Translators: message presented when the text cannot be added to the clipboard.
			ui.message(_("Cannot add"))

	def script_add(self, gesture):
		if config.conf["clipContentsDesigner"]["confirmToAdd"]:
			wx.CallAfter(self.confirmAdd)
		else:
			self.performAdd()
	# Translators: message presented in input mode.
	script_add.__doc__ = _("Retrieves the selected string or the text from the previously set start marker up to and including the current position of the review cursor, and adds it to the clipboard.")

	def script_clear(self, gesture):
		self.clearClipboard()
	# Translators: message presented in input mode.
	script_clear.__doc__ = _("Deletes the added text and the content of the clipboard.")

	__gestures = {
		"kb:NVDA+windows+c": "add",
		"kb:NVDA+windows+x": "clear",
		"kb:NVDA+windows+f9": "setSelectionStartMarker",
	}

class AddonSettingsDialog(SettingsDialog):

	# Translators: title of a dialog.
	title = _("Clip Contents Designer settings")

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
		self.confirmAddCheckBox = sHelper.addItem(wx.CheckBox(self, label= _("Confirm to &add text")))
		self.confirmAddCheckBox.SetValue(config.conf["clipContentsDesigner"]["confirmToAdd"])
		# Translators: label of a dialog.
		self.confirmCleanCheckBox = sHelper.addItem(wx.CheckBox(self, label= _("Confirm to c&leanup clipboard")))
		self.confirmCleanCheckBox.SetValue(config.conf["clipContentsDesigner"]["confirmToClean"])
		# Translators: label of a dialog.
		self.confirmCopyCheckBox = sHelper.addItem(wx.CheckBox(self, label= _("&Confirm to copy text")))
		self.confirmCopyCheckBox.SetValue(config.conf["clipContentsDesigner"]["confirmToCopy"])

	def postInit(self):
		self.setSeparatorEdit.SetFocus()

	def onOk(self,evt):
		super(AddonSettingsDialog, self).onOk(evt)
		config.conf["clipContentsDesigner"]["separator"] = self.setSeparatorEdit.GetValue()
		config.conf["clipContentsDesigner"]["addTextBefore"] = self.addTextBeforeCheckBox.GetValue()
		config.conf["clipContentsDesigner"]["confirmToAdd"] = self.confirmAddCheckBox.GetValue()
		config.conf["clipContentsDesigner"]["confirmToClean"] = self.confirmCleanCheckBox.GetValue()
		config.conf["clipContentsDesigner"]["confirmToCopy"] = self.confirmCopyCheckBox.GetValue()

