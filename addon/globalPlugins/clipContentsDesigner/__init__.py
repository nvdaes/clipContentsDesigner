# -*- coding: UTF-8 -*-
# clipContentsDesigner: a global plugin for managing clipboard text
# Copyright (C) 2012-2021 Noelia Ruiz Martínez, other contributors
# Released under GPL 2

import addonHandler
import globalPluginHandler
import api
import textInfos
import controlTypes
import ui
import winUser
import browseMode
import config
import core
import wx
import gui
from gui import SettingsPanel, NVDASettingsDialog, guiHelper
from keyboardHandler import KeyboardInputGesture
from scriptHandler import script
from logHandler import log
from typing import Callable, Optional

addonHandler.initTranslation()

_: Callable[[str], str]

# Constants

ADDON_NAME = addonHandler.getCodeAddon().name
ADDON_SUMMARY = addonHandler.getCodeAddon().manifest["summary"]
ADDON_PANEL_TITLE = ADDON_SUMMARY
BROWSEABLETEXT_FORMATS = [
	# Translators: label of a dialog.
	_("Preformatted text in HTML"),
	# Translators: label of a dialog.
	_("HTML as shown in a web browser")
]
# Translators: Text of the clipboard shown without being formatted.
RAW_TEXT = _("Plain text")

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
config.conf.spec[ADDON_NAME] = confspec


def getBookmark() -> str:
	try:
		separator = config.conf[ADDON_NAME]["separator"]
	except KeyError:
		separator = None
	if not separator:
		bookmark = "\r\n"
	else:
		bookmark = f"\r\n{separator}\r\n"
	return bookmark


def isArabicKeyboardLayout() -> bool:
	"""
	Test if the keyboard layout is Arabic to avoid an error reported by a user.
	"""
	import locale
	curWindow = winUser.getForegroundWindow()
	threadID = winUser.getWindowThreadProcessID(curWindow)[1]
	klID = winUser.getKeyboardLayout(threadID)
	lID = klID & (2**16 - 1)
	try:
		localeName: Optional[str] = locale.windows_locale[lID]
	except KeyError:
		localeName = None
	if localeName and localeName.startswith("ar_"):
		return True
	return False


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	scriptCategory = ADDON_SUMMARY

	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		NVDASettingsDialog.categoryClasses.append(AddonSettingsPanel)

	def terminate(self):
		NVDASettingsDialog.categoryClasses.remove(AddonSettingsPanel)

	def onSettings(self, evt):
		gui.mainFrame._popupSettingsDialog(NVDASettingsDialog, AddonSettingsPanel)

	@script(
		# Translators: message presented in input mode.
		description=_("Shows the Clip Contents Designer settings."),
	)
	def script_settings(self, gesture):
		wx.CallAfter(self.onSettings, None)

	def clearClipboard(self) -> None:
		try:
			with winUser.openClipboard(gui.mainFrame.Handle):
				winUser.emptyClipboard()
			# Translators: message presented when the clipboard content has been deleted.
			ui.message(_("Clipboard cleared"))
		except Exception as e:
			# Translators: message presented when the clipboard content cannot be deleted.
			ui.message(_("Clipboard not cleared"))
			log.debug(f"Cannot clear clipboard: {e}")

	def getSelectedText(self) -> str:
		obj = api.getFocusObject()
		treeInterceptor = obj.treeInterceptor
		if isinstance(treeInterceptor, browseMode.BrowseModeDocumentTreeInterceptor):
			obj = treeInterceptor
		try:
			info = obj.makeTextInfo(textInfos.POSITION_SELECTION)
		except (RuntimeError, NotImplementedError):
			info = None
		if not info or info.isCollapsed:
			return ""
		return info.clipboardText

	def getMath(self) -> str:
		import mathPres
		mathMl = mathPres.getMathMlFromTextInfo(api.getReviewPosition())
		if not mathMl:
			obj = api.getNavigatorObject()
			if obj.role == controlTypes.ROLE_MATH:
				try:
					mathMl = obj.mathMl
				except (NotImplementedError, LookupError):
					mathMl = None
		if not mathMl:
			return ""
		mathPres.ensureInit()
		if mathPres.brailleProvider:
			text = mathPres.brailleProvider.getBrailleForMathMl(mathMl)
			return text
		return ""

	def getTextToAdd(self) -> Optional[str]:
		newText: str = self.getSelectedText() or self.getMath()
		if not newText:
			if not getattr(
				api.getReviewPosition().obj,
				"_selectThenCopyRange", None
			) or not api.getReviewPosition().obj._selectThenCopyRange:
				# Translators: message presented when it's not possible to add text, since no text has been selected.
				ui.message(_("No text to add"))
				return None
			newText = api.getReviewPosition().obj._selectThenCopyRange.clipboardText
		try:
			clipData: str = api.getClipData()
		except Exception:
			clipData = ""
			
		text: str
		if len(clipData) > 0:
			if config.conf[ADDON_NAME]["addTextBefore"]:
				text = newText + getBookmark() + clipData
			else:
				text = clipData + getBookmark() + newText
		else:
			text = newText
		return text

	def clipboardHasContent(self) -> bool:
		with winUser.openClipboard(gui.mainFrame.Handle):
			clipFormat = winUser.windll.user32.EnumClipboardFormats(0)
		if clipFormat:
			return True
		return False

	def requiredFormatInClip(self) -> bool:
		if config.conf[ADDON_NAME]["confirmationRequirement"] == 0:
			return True
		if config.conf[ADDON_NAME]["confirmationRequirement"] == 1:
			try:
				api.getClipData()
				return True
			except Exception:
				return False
		if self.clipboardHasContent():
			return True
		return False

	def confirmAdd(self) -> None:
		text = self.getTextToAdd()
		if not text:
			return
		if gui.messageBox(
			# Translators: Label of a dialog.
			_("Please, confirm if you want to add text to the clipboard"),
			# Translators: Title of a dialog.
			_("Adding text to clipboard"),
			wx.OK | wx.CANCEL
		) == wx.OK:
			if api.copyToClip(text):
				# Translators: message presented when the text has been added to the clipboard.
				core.callLater(200, ui.message, _("Added"))
			else:
				# Translators: message presented when the text cannot be added to the clipboard.
				core.callLater(200, ui.message, _("Cannot add"))

	def performAdd(self) -> None:
		text = self.getTextToAdd()
		if api.copyToClip(text):
			# Translators: message presented when the text has been added to the clipboard.
			ui.message(_("Added"))
		else:
			# Translators: message presented when the text cannot be added to the clipboard.
			ui.message(_("Cannot add"))

	@script(
		# Translators: message presented in input mode.
		description=_("""Retrieves the selected string or the text from the previously set start marker up to
		and including the current position of the review cursor, and adds it to the clipboard."""),
		gesture="kb:NVDA+windows+c"
	)
	def script_add(self, gesture):
		if (
			config.conf["clipContentsDesigner"]["confirmToAdd"] and not gui.isInMessageBox
			and self.requiredFormatInClip()
		):
			wx.CallAfter(self.confirmAdd)
		else:
			self.performAdd()

	def confirmClear(self) -> None:
		if gui.messageBox(
			# Translators: Label of a dialog.
			_("Please, confirm if you want to clear the clipboard"),
			# Translators: Title of a dialog.
			_("Clearing clipboard"),
			wx.OK | wx.CANCEL
		) != wx.OK:
			return
		self.clearClipboard()

	@script(
		# Translators: message presented in input mode.
		description=_("Deletes the added text and the content of the clipboard."),
		gesture="kb:NVDA+windows+x"
	)
	def script_clear(self, gesture):
		if (
			config.conf["clipContentsDesigner"]["confirmToClear"]
			and not gui.isInMessageBox and self.requiredFormatInClip()
		):
			wx.CallAfter(self.confirmClear)
		else:
			self.clearClipboard()

	def copy(self) -> None:
		obj = api.getFocusObject()
		tI = obj.treeInterceptor
		if isinstance(tI, browseMode.BrowseModeDocumentTreeInterceptor) and not tI.passThrough:
			tI.script_copyToClipboard(None)
		else:
			keyName = "control+c" if not isArabicKeyboardLayout() else u"control+ؤ"
			KeyboardInputGesture.fromName(keyName).send()

	def confirmCopy(self) -> None:
		text = self.getSelectedText()
		if gui.messageBox(
			# Translators: Label of a dialog.
			_("Please, confirm if you want to copy to the clipboard"),
			# Translators: Title of a dialog.
			_("Copying to clipboard"),
			wx.OK | wx.CANCEL
		) != wx.OK:
			return
		if text:
			api.copyToClip(text)
		else:
			core.callLater(200, self.copy)

	@script(
		# Translators: message presented in input mode.
		description=_("Copies to the clipboard, with the possibility of being asked for a previous confirmation")
	)
	def script_copy(self, gesture):
		if (
			config.conf[ADDON_NAME]["confirmToCopy"]
			and not gui.isInMessageBox and self.requiredFormatInClip()
		):
			wx.CallAfter(self.confirmCopy)
		else:
			self.copy()

	def cut(self) -> None:
		keyName = "control+x" if not isArabicKeyboardLayout() else u"control+ء"
		KeyboardInputGesture.fromName(keyName).send()

	def confirmCut(self) -> None:
		if gui.messageBox(
			# Translators: Label of a dialog.
			_("Please, confirm if you want to cut from the clipboard"),
			# Translators: Title of a dialog.
			_("Cutting from clipboard"),
			wx.OK | wx.CANCEL
		) != wx.OK:
			return
		core.callLater(200, self.cut)

	@script(
		# Translators: message presented in input mode.
		description=_("Cuts from the clipboard, with the possibility of being asked for a previous confirmation")
	)
	def script_cut(self, gesture):
		if (
			config.conf["clipContentsDesigner"]["confirmToCut"]
			and not gui.isInMessageBox and self.requiredFormatInClip()
		):
			wx.CallAfter(self.confirmCut)
		else:
			self.cut()

	@script(
		# Translators: message presented in input mode.
		description=_("Shows the clipboard text as HTML in browse mode")
	)
	def script_showClipboardText(self, gesture):
		try:
			text = api.getClipData()
		except Exception:
			text = None
		if not text:
			if self.clipboardHasContent():
				# Translators: presented when clipboard is not empty, but there is no text to show in browse mode.
				ui.message(_("Clipboard is not empty, but there is no text to show"))
			else:
				# Translators: presented when clipboard is empty.
				ui.message(_("Clipboard is empty"))
		else:
			if (
				config.conf[ADDON_NAME]["maxLengthForBrowseableText"] <= len(text)
			):
				maxLength = config.conf[ADDON_NAME]["maxLengthForBrowseableText"]
			else:
				maxLength = len(text)
			format = config.conf["clipContentsDesigner"]["browseableTextFormat"]
			html = True
			if format == 0:
				browseableText = f"<pre>{text.strip()[:maxLength]}</pre>"
			else:
				browseableText = text.strip()[:maxLength]
			ui.browseableMessage(
				browseableText,
				# Translators: title of a browseable message.
				_("Clipboard text ({max}/{current} - {formatForTitle})".format(
					max=maxLength, current=len(text), formatForTitle=BROWSEABLETEXT_FORMATS[format]
				)), html)

	@script(
		# Translators: message presented in input mode.
		description=_("Shows the clipboard textual contents as plain text in browse mode")
	)
	def script_showClipboardRawText(self, gesture):
		try:
			text = api.getClipData()
		except Exception:
			text = None
		if not text:
			if self.clipboardHasContent():
				# Translators: presented when clipboard is not empty, but there is no text to show in browse mode.
				ui.message(_("Clipboard is not empty, but there is no text to show"))
			else:
				# Translators: presented when clipboard is empty.
				ui.message(_("Clipboard is empty"))
		else:
			if (
				config.conf[ADDON_NAME]["maxLengthForBrowseableText"] <= len(text)
			):
				maxLength = config.conf[ADDON_NAME]["maxLengthForBrowseableText"]
			else:
				maxLength = len(text)
			browseableText = text.strip()[:maxLength]
			ui.browseableMessage(
				browseableText,
				# Translators: title of a browseable message.
				_("Clipboard text ({max}/{current} - {formatForTitle})".format(
					max=maxLength, current=len(text), formatForTitle=RAW_TEXT
				)), False)


class AddonSettingsPanel(SettingsPanel):

	title = ADDON_PANEL_TITLE

	def makeSettings(self, settingsSizer):
		sHelper = guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		# Translators: label of a dialog.
		setSeparatorLabel = _("Type the string to be used as a &separator between contents added to the clipboard.")
		self.setSeparatorEdit = sHelper.addLabeledControl(setSeparatorLabel, wx.TextCtrl)
		try:
			self.setSeparatorEdit.SetValue(config.conf[ADDON_NAME]["separator"])
		except KeyError:
			pass
		# Translators: label of a dialog.
		self.addTextBeforeCheckBox = sHelper.addItem(wx.CheckBox(self, label=_("&Add text before clip data")))
		self.addTextBeforeCheckBox.SetValue(config.conf[ADDON_NAME]["addTextBefore"])
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
		self.confirmList = sHelper.addLabeledControl(
			confirmBoxLabel, gui.nvdaControls.CustomCheckListBox, choices=confirmChoices
		)
		checkedItems = []
		confirmationItems = ("confirmToAdd", "confirmToClear", "confirmToCopy", "confirmToCut")
		for k, v in config.conf[ADDON_NAME].items:
			if k not in confirmationItems or not v:
				continue
			checkedItems.append(confirmationItems.index(k))
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
		self.confirmRequirementChoices = sHelper.addLabeledControl(
			confirmRequirementsLabel, wx.Choice, choices=requirementChoices
		)
		self.confirmRequirementChoices.SetSelection(config.conf["clipContentsDesigner"]["confirmationRequirement"])
		# Translators: label of a dialog.
		formatLabel = _("&Format to show the clipboard text as HTML in browse mode:")
		self.formatChoices = sHelper.addLabeledControl(formatLabel, wx.Choice, choices=BROWSEABLETEXT_FORMATS)
		self.formatChoices.SetSelection(config.conf[ADDON_NAME]["browseableTextFormat"])
		# Translators: label of a dialog.
		maxLengthLabel = _("&Maximum number of characters when showing clipboard text in browse mode")
		self.maxLengthEdit = sHelper.addLabeledControl(
			maxLengthLabel,
			gui.nvdaControls.SelectOnFocusSpinCtrl,
			min=1,
			max=1000000,
			initial=config.conf[ADDON_NAME]["maxLengthForBrowseableText"]
		)

	def postInit(self):
		self.setSeparatorEdit.SetFocus()

	def onSave(self):
		config.conf[ADDON_NAME]["separator"] = self.setSeparatorEdit.GetValue()
		config.conf[ADDON_NAME]["addTextBefore"] = self.addTextBeforeCheckBox.GetValue()
		config.conf[ADDON_NAME]["confirmToAdd"] = self.confirmList.IsChecked(0)
		config.conf[ADDON_NAME]["confirmToClear"] = self.confirmList.IsChecked(1)
		config.conf[ADDON_NAME]["confirmToCopy"] = self.confirmList.IsChecked(2)
		config.conf[ADDON_NAME]["confirmToCut"] = self.confirmList.IsChecked(3)
		config.conf[ADDON_NAME]["confirmationRequirement"] = (
			self.confirmRequirementChoices.GetSelection()
		)
		config.conf[ADDON_NAME]["browseableTextFormat"] = (
			self.formatChoices.GetSelection()
		)
		config.conf[ADDON_NAME]["maxLengthForBrowseableText"] = (
			self.maxLengthEdit.GetValue()
		)
