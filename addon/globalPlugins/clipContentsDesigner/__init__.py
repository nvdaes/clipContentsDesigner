# clipContentsDesigner: a global plugin for managing clipboard text
# Copyright (C) 2012-2025 Noelia Ruiz Martínez, other contributors
# Released under GPL 2

import addonHandler
import globalPluginHandler
import globalVars
import api
import textInfos
import controlTypes
import ui
import winUser
import browseMode
import config
import core
import wx  # type: ignore[reportMissingModuleSource]
import gui
import gui.guiHelper as guiHelper
from gui.settingsDialogs import SettingsPanel, NVDASettingsDialog
from gui.message import MessageDialog, ReturnCode
from keyboardHandler import KeyboardInputGesture
from typing import Any
from scriptHandler import script
from logHandler import log
import locale
from ui import browseableMessage

addonHandler.initTranslation()

# Constants

ADDON_SUMMARY: str = addonHandler.getCodeAddon().manifest["summary"]
ADDON_PANEL_TITLE: str = ADDON_SUMMARY
BROWSEABLETEXT_FORMATS: list[str] = [
	# Translators: label of a dialog.
	_("Preformatted text in HTML"),
	# Translators: label of a dialog.
	_("HTML as shown in a web browser"),
]
# Translators: Text of the clipboard shown without being formatted.
RAW_TEXT: str = _("Plain text")

confspec: dict[str, str] = {
	"separator": "string(default='')",
	"addTextBefore": "boolean(default=False)",
	"confirmToAdd": "boolean(default=False)",
	"confirmToClear": "boolean(default=False)",
	"confirmToCopy": "boolean(default=False)",
	"confirmToCut": "boolean(default=False)",
	"confirmationRequirement": "integer(default=0)",
	"browseableTextFormat": "integer(default=0)",
	"maxLengthForBrowseableText": "integer(default=100000)",
	"runOnInstall": "boolean(default=True)",
}
config.conf.spec["clipContentsDesigner"] = confspec


def getBookmark() -> str:
	separator = config.conf["clipContentsDesigner"]["separator"]
	if not separator:
		bookmark = "\r\n"
	else:
		bookmark = "\r\n%s\r\n" % separator
	return bookmark


def getKeyboardLayout() -> str | None:
	curWindow = winUser.getForegroundWindow()
	threadID = winUser.getWindowThreadProcessID(curWindow)[1]
	klID = winUser.getKeyboardLayout(threadID)
	lID = klID & (2**16 - 1)
	try:
		localeName = locale.windows_locale[lID]
	except KeyError:
		localeName = None
	return localeName


def getKeyForCopy() -> str:
	"""
	Test the keyboard layout and return correct keyName for copying
	"""
	keyboardLayout = getKeyboardLayout()
	if keyboardLayout and keyboardLayout.startswith("fa_"):
		return "control+ز"
	elif keyboardLayout and keyboardLayout.startswith("ar_"):
		return "control+ؤ"
	elif keyboardLayout and keyboardLayout.startswith("he_"):
		return "control+ב"
	else:
		return "control+c"


def getKeyForCut() -> str:
	"""
	Test the keyboard layout and return correct keyName for cutting
	"""
	keyboardLayout = getKeyboardLayout()
	if keyboardLayout and keyboardLayout.startswith("fa_"):
		return "control+ط"
	elif keyboardLayout and keyboardLayout.startswith("ar_"):
		return "control+ء"
	else:
		return "control+x"


def disableInSecureMode(decoratedCls: type[Any]) -> type[Any]:
	if globalVars.appArgs.secure:
		return globalPluginHandler.GlobalPlugin
	return decoratedCls


@disableInSecureMode
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	scriptCategory = ADDON_SUMMARY

	def __init__(self) -> None:
		super().__init__()
		NVDASettingsDialog.categoryClasses.append(AddonSettingsPanel)

	def terminate(self) -> None:  # type: ignore[reportImplicitOverride]
		NVDASettingsDialog.categoryClasses.remove(AddonSettingsPanel)

	def onSettings(self, evt: object) -> None:
		gui.mainFrame.popupSettingsDialog(NVDASettingsDialog, AddonSettingsPanel)

	@script(
		# Translators: message presented in input mode.
		description=_("Shows the Clip Contents Designer settings."),
	)
	def script_settings(self, gesture: KeyboardInputGesture) -> None:
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
			log.debug("Cannot clear clipboard: %s" % e)

	def getSelectedText(self) -> str | None:
		obj = api.getFocusObject()
		treeInterceptor = obj.treeInterceptor
		if isinstance(treeInterceptor, browseMode.BrowseModeDocumentTreeInterceptor):
			obj = treeInterceptor
		try:
			info = obj.makeTextInfo(textInfos.POSITION_SELECTION)  # type: ignore[reportAttributeAccessIssue]
		except (RuntimeError, NotImplementedError):
			info = None
		if not info or info.isCollapsed:  # type: ignore[reportUnknownMemberType]
			return None
		return info.clipboardText  # type: ignore[reportUnknownMemberType,reportUnknownVariableType]

	def getMath(self) -> str | None:
		import mathPres

		mathMl = mathPres.getMathMlFromTextInfo(api.getReviewPosition())
		if not mathMl:
			obj = api.getNavigatorObject()
			if obj.role == controlTypes.Role.MATH:
				try:
					mathMl = obj.mathMl
				except (NotImplementedError, LookupError):
					mathMl = None
		if not mathMl:
			return None
		if mathPres.brailleProvider:
			text = mathPres.brailleProvider.getBrailleForMathMl(mathMl)
			return text
		return None
	def getTextToAdd(self) -> str | None:
		newText = self.getSelectedText() or self.getMath()
		if not newText:
			if (
				not getattr(
					api.getReviewPosition().obj,
					"_selectThenCopyRange",
					None,
				)
				or not api.getReviewPosition().obj._selectThenCopyRange
			):
				return
			newText = api.getReviewPosition().obj._selectThenCopyRange.clipboardText
		try:
			clipData = api.getClipData()
		except Exception:
			clipData = None
		if clipData:
			if config.conf["clipContentsDesigner"]["addTextBefore"]:
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
		if config.conf["clipContentsDesigner"]["confirmationRequirement"] == 0:
			return True
		if config.conf["clipContentsDesigner"]["confirmationRequirement"] == 1:
			try:
				_unused = api.getClipData()  # noqa: F841
				return True
			except Exception:
				return False
		if self.clipboardHasContent():
			return True
		return False

	@gui.blockAction.when(gui.blockAction.Context.MODAL_DIALOG_OPEN)
	def confirmAdd(self) -> None:
		text = self.getTextToAdd()
		if not text:
			return
		if (
			MessageDialog.confirm(  # type: ignore[reportUnknownMemberType]
				# Translators: Label of a dialog.
				_("Please, confirm if you want to add text to the clipboard"),
				# Translators: Title of a dialog.
				_("Adding text to clipboard"),
			)
			== ReturnCode.OK
		):
			if api.copyToClip(text):
				# Translators: message presented when the text has been added to the clipboard.
				_unused = core.callLater(200, ui.message, _("Added"))  # noqa: F841
			else:
				# Translators: message presented when the text cannot be added to the clipboard.
				_unused = core.callLater(200, ui.message, _("Cannot add"))  # noqa: F841

	def performAdd(self) -> None:
		text = self.getTextToAdd()
		if text and api.copyToClip(text):
			# Translators: message presented when the text has been added to the clipboard.
			ui.message(_("Added"))
		else:
			# Translators: message presented when the text cannot be added to the clipboard.
			ui.message(_("Cannot add"))

	@script(
		description=_(
			# Translators: message presented in input mode.
			"Retrieves the selected string or the text from the previously set start marker up to "
			+ "and including the current position of the review cursor, and adds it to the clipboard."
		),
		gesture="kb:NVDA+windows+c",
	)
	def script_add(self, gesture: KeyboardInputGesture) -> None:
		if config.conf["clipContentsDesigner"]["confirmToAdd"] and self.requiredFormatInClip():
			wx.CallAfter(self.confirmAdd)
		else:
			self.performAdd()

	@gui.blockAction.when(gui.blockAction.Context.MODAL_DIALOG_OPEN)
	def confirmClear(self) -> None:
		if (
			MessageDialog.confirm(  # type: ignore[reportUnknownMemberType]
				# Translators: Label of a dialog.
				_("Please, confirm if you want to clear the clipboard"),
				# Translators: Title of a dialog.
				_("Clearing clipboard"),
			)
			!= ReturnCode.OK
		):
			return
		self.clearClipboard()

	@script(
		# Translators: message presented in input mode.
		description=_("Deletes the added text and the content of the clipboard."),
		gesture="kb:NVDA+windows+x",
	)
	def script_clear(self, gesture: KeyboardInputGesture) -> None:
		if config.conf["clipContentsDesigner"]["confirmToClear"]:
			wx.CallAfter(self.confirmClear)
		else:
			self.clearClipboard()

	def copy(self) -> None:
		keyName = getKeyForCopy()
		gesture = KeyboardInputGesture.fromName(keyName)
		obj = api.getFocusObject()
		tI = obj.treeInterceptor
		if isinstance(tI, browseMode.BrowseModeDocumentTreeInterceptor) and not tI.passThrough:
			tI.script_copyToClipboard(gesture)
		else:
			_unused = gesture.send()  # noqa: F841

	@gui.blockAction.when(gui.blockAction.Context.MODAL_DIALOG_OPEN)
	def confirmCopy(self) -> None:
		if (
			MessageDialog.confirm(  # type: ignore[reportUnknownMemberType]
				# Translators: Label of a dialog.
				_("Please, confirm if you want to copy to the clipboard"),
				# Translators: Title of a dialog.
				_("Copying to clipboard"),
			)
			!= ReturnCode.OK
		):
			return
		_unused = core.callLater(200, self.copy)  # noqa: F841

	@script(
		description=_(
			# Translators: message presented in input mode.
			"Copies to the clipboard, with the possibility of being asked for a previous confirmation",
		),
	)
	def script_copy(self, gesture: KeyboardInputGesture) -> None:
		if config.conf["clipContentsDesigner"]["confirmToCopy"] and self.requiredFormatInClip():
			wx.CallAfter(self.confirmCopy)
		else:
			self.copy()

	def cut(self) -> None:
		keyName = getKeyForCut()
		KeyboardInputGesture.fromName(keyName).send()

	@gui.blockAction.when(gui.blockAction.Context.MODAL_DIALOG_OPEN)
	def confirmCut(self) -> None:
		if (
			MessageDialog.confirm(  # type: ignore[reportUnknownMemberType]
				# Translators: Label of a dialog.
				_("Please, confirm if you want to cut from the clipboard"),
				# Translators: Title of a dialog.
				_("Cutting from clipboard"),
			)
			!= ReturnCode.OK
		):
			return
		_unused = core.callLater(200, self.cut)  # noqa: F841

	@script(
		description=_(
			# Translators: message presented in input mode.
			"Cuts from the clipboard, with the possibility of being asked for a previous confirmation",
		),
	)
	def script_cut(self, gesture: KeyboardInputGesture) -> None:
		if config.conf["clipContentsDesigner"]["confirmToCut"] and self.requiredFormatInClip():
			wx.CallAfter(self.confirmCut)
		else:
			self.cut()

	@script(
		# Translators: message presented in input mode.
		description=_("Shows the clipboard text as HTML in browse mode"),
	)
	def script_showClipboardText(self, gesture: KeyboardInputGesture) -> None:
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
			if config.conf["clipContentsDesigner"]["maxLengthForBrowseableText"] <= len(text):
				maxLength = config.conf["clipContentsDesigner"]["maxLengthForBrowseableText"]
			else:
				maxLength = len(text)
			format = config.conf["clipContentsDesigner"]["browseableTextFormat"]
			html = True
			if format == 0:
				browseableText = "<pre>%s</pre>" % text.strip()[:maxLength]
			else:
				browseableText = text.strip()[:maxLength]
			browseableMessage(
				browseableText,
				_(
					# Translators: title of a browseable message.
					"Clipboard text ({max}/{current} - {formatForTitle})".format(
						max=maxLength,
						current=len(text),
						formatForTitle=BROWSEABLETEXT_FORMATS[format],
					),
				),
				html,
				closeButton=True,
			)

	@script(
		# Translators: message presented in input mode.
		description=_("Shows the clipboard textual contents as plain text in browse mode"),
	)
	def script_showClipboardRawText(self, gesture: KeyboardInputGesture) -> None:
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
			if config.conf["clipContentsDesigner"]["maxLengthForBrowseableText"] <= len(text):
				maxLength = config.conf["clipContentsDesigner"]["maxLengthForBrowseableText"]
			else:
				maxLength = len(text)
			browseableText = text.strip()[:maxLength]
			browseableMessage(
				browseableText,
				# Translators: title of a browseable message.
				_(
					"Clipboard text ({max}/{current} - {formatForTitle})".format(
						max=maxLength,
						current=len(text),
						formatForTitle=RAW_TEXT,
					),
				),
				False,
				closeButton=True,
			)


class AddonSettingsPanel(SettingsPanel):
	title: str = ADDON_PANEL_TITLE
	setSeparatorEdit: wx.TextCtrl
	addTextBeforeCheckBox: wx.CheckBox
	confirmList: gui.nvdaControls.CustomCheckListBox
	confirmRequirementChoices: wx.Choice
	formatChoices: wx.Choice
	maxLengthEdit: gui.nvdaControls.SelectOnFocusSpinCtrl
	runOnInstallCheckBox: wx.CheckBox
	restoreDefaultsButton: wx.Button

	def makeSettings(self, sizer: object) -> None:  # type: ignore[reportImplicitOverride]
		sHelper = guiHelper.BoxSizerHelper(self, sizer=sizer)
		setSeparatorLabel = _(
			# Translators: label of a dialog.
			"Type the string to be used as a &separator between contents added to the clipboard.",
		)
		self.setSeparatorEdit = sHelper.addLabeledControl(setSeparatorLabel, wx.TextCtrl)  # type: ignore[reportUnknownMemberType]
		self.setSeparatorEdit.SetValue(config.conf["clipContentsDesigner"]["separator"])
		# Translators: label of a dialog.
		self.addTextBeforeCheckBox = sHelper.addItem(wx.CheckBox(self, label=_("&Add text before clip data")))  # type: ignore[reportUnknownMemberType]
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
		self.confirmList = sHelper.addLabeledControl(  # type: ignore[reportUnknownMemberType]
			confirmBoxLabel,
			gui.nvdaControls.CustomCheckListBox,
			choices=confirmChoices,
		)
		checkedItems: list[int] = []
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
		self.confirmRequirementChoices = sHelper.addLabeledControl(  # type: ignore[reportUnknownMemberType]
			confirmRequirementsLabel,
			wx.Choice,
			choices=requirementChoices,
		)
		self.confirmRequirementChoices.SetSelection(
			config.conf["clipContentsDesigner"]["confirmationRequirement"],
		)
		# Translators: label of a dialog.
		formatLabel = _("&Format to show the clipboard text as HTML in browse mode:")
		self.formatChoices = sHelper.addLabeledControl(formatLabel, wx.Choice, choices=BROWSEABLETEXT_FORMATS)  # type: ignore[reportUnknownMemberType]
		self.formatChoices.SetSelection(config.conf["clipContentsDesigner"]["browseableTextFormat"])
		# Translators: label of a dialog.
		maxLengthLabel = _("&Maximum number of characters when showing clipboard text in browse mode")
		self.maxLengthEdit = sHelper.addLabeledControl(  # type: ignore[reportUnknownMemberType]
			maxLengthLabel,
			gui.nvdaControls.SelectOnFocusSpinCtrl,
			min=1,
			max=1000000,
			initial=config.conf["clipContentsDesigner"]["maxLengthForBrowseableText"],
		)
		self.runOnInstallCheckBox = sHelper.addItem(  # type: ignore[reportUnknownMemberType]
			# Translators: label of a dialog.
			wx.CheckBox(self, label=_("Show configuration dialog when &updating")),
		)
		self.runOnInstallCheckBox.SetValue(config.conf["clipContentsDesigner"]["runOnInstall"])
		# Translators: label of a dialog.
		self.restoreDefaultsButton = sHelper.addItem(wx.Button(self, label=_("Restore defaults")))  # type: ignore[reportUnknownMemberType]
		self.restoreDefaultsButton.Bind(wx.EVT_BUTTON, self.onRestoreDefaults)

	def onRestoreDefaults(self, evt: object) -> None:
		self.setSeparatorEdit.SetValue(
			config.conf.getConfigValidation(["clipContentsDesigner", "separator"]).default,
		)
		self.addTextBeforeCheckBox.SetValue(
			config.conf.getConfigValidation(["clipContentsDesigner", "addTextBefore"]).default,
		)
		self.confirmList.CheckedItems = []
		self.confirmRequirementChoices.SetSelection(
			config.conf.getConfigValidation(["clipContentsDesigner", "confirmationRequirement"]).default,
		)
		self.formatChoices.SetSelection(
			config.conf.getConfigValidation(["clipContentsDesigner", "browseableTextFormat"]).default,
		)
		self.maxLengthEdit.SetValue(
			config.conf.getConfigValidation(["clipContentsDesigner", "maxLengthForBrowseableText"]).default,
		)
		self.runOnInstallCheckBox.SetValue(
			config.conf.getConfigValidation(["clipContentsDesigner", "runOnInstall"]).default,
		)

	def onSave(self) -> None:  # type: ignore[reportImplicitOverride]
		config.conf["clipContentsDesigner"]["separator"] = self.setSeparatorEdit.GetValue()
		config.conf["clipContentsDesigner"]["addTextBefore"] = self.addTextBeforeCheckBox.GetValue()
		config.conf["clipContentsDesigner"]["confirmToAdd"] = self.confirmList.IsChecked(0)
		config.conf["clipContentsDesigner"]["confirmToClear"] = self.confirmList.IsChecked(1)
		config.conf["clipContentsDesigner"]["confirmToCopy"] = self.confirmList.IsChecked(2)
		config.conf["clipContentsDesigner"]["confirmToCut"] = self.confirmList.IsChecked(3)
		config.conf["clipContentsDesigner"]["confirmationRequirement"] = (
			self.confirmRequirementChoices.GetSelection()
		)
		config.conf["clipContentsDesigner"]["browseableTextFormat"] = self.formatChoices.GetSelection()
		config.conf["clipContentsDesigner"]["maxLengthForBrowseableText"] = self.maxLengthEdit.GetValue()
		config.conf["clipContentsDesigner"]["runOnInstall"] = self.runOnInstallCheckBox.GetValue()
