# -*- coding: UTF-8 -*-

# clipContentsDesigner: a global plugin for managing clipboard text
# Version: 3.0
# Added option of copying the separator to import when reinstalling the add-on, suggested by Joseph Lee
# Date: 07/06/2015
# Just use a single new line to separate appended strings when no separator is set, suggested by Bhavya
# Date: 05/06/2015
# Braille representation for math can be appended to the clipboard
# Date: 03/06/2015

# Version: 2.0
# Hindi characters can be writen as a separator
# Date: 27/02/2015
# Version: 1.0
# Changed menu labels according to the new add-on name
# Date: 3/07/2014
# Revision and improvements: Mesar Hameed
# Date: 20/09/2014
# Added scriptCategory
# Added msg plugin, developed by Alberto Buffolino
# Date: 21/09/2014
# Minor changes in messages according to new add-on name
# Date: 12, 13/12/2014
# Changed keyboard commands according to Bhavya's suggestions
# Date: 13/12/2014
# Implemented several suggestions from "Alberto Buffolino
# Date: 14/12/2014

# Append text: a global plugin for appending text to the clipboard

# Version: 1.1
# Bug fixed: added control in gestures. Now NVDA+shift+c can be used in Excel tables
# Date: 30/01/2013
# Version: 1.0
# Date: 28/12/2012

import addonHandler
import globalPluginHandler
import api
import textInfos
import ui
import msg # Developed by Alberto Bufolino
import win32clipboard
import os
import shutil
import globalVars
import wx
import gui
from gui import SettingsDialog
from logHandler import log
from cStringIO import StringIO
from configobj import ConfigObj
from validate import Validator

addonHandler.initTranslation()

try:
	from globalCommands import SCRCAT_TEXTREVIEW, SCRCAT_CONFIG
except:
	SCRCAT_TEXTREVIEW = SCRCAT_CONFIG = None

iniFileName = os.path.join(os.path.dirname(__file__), "clipContentsDesigner.ini")

confspec = ConfigObj(StringIO("""#Configuration file

[separator]
	bookmarkSeparator = string(default="")
"""), encoding="UTF-8")
confspec.newlines = "\r\n"
conf = ConfigObj(iniFileName, configspec = confspec, indent_type = "\t", encoding="UTF-8")
val = Validator()
conf.validate(val)

def getBookmark():
	if conf["separator"]["bookmarkSeparator"] == "":
		bookmark = "\r\n"
	else:
		bookmark = "\r\n%s\r\n" % conf["separator"]["bookmarkSeparator"]
	return bookmark

bookmark = getBookmark()

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
	script_settings.__doc__ = _("Shows the Clip Contents Designer settings dialog")

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

	def script_append(self, gesture):
		newText = self.getSelectedText() or self.getMath()
		if not newText:
			if not self._copyStartMarker:
				# Translators: message presented when it's not possible to append text, since no text has been selected or marked.
				ui.message(_("No selection. No start marker set"))
				return
			pos = api.getReviewPosition().copy()
			if self._copyStartMarker.obj != pos.obj:
				# Translators: message presented when user tries to select text across object boundaries
				msg.message(_("The start marker must reside within the same object"))
				return
			pos.move(textInfos.UNIT_CHARACTER, 1, endPoint="end")
			pos.setEndPoint(self._copyStartMarker, "startToStart")
			if not pos.compareEndPoints(pos, "startToEnd") < 0:
				# Translators: message presented when review cursor has been used to append text and there is no text to append.
				ui.message(_("No text to append"))
				return
			newText = pos.clipboardText
			self._copyStartMarker = None
		try:
			clipData = api.getClipData()
			text = clipData+bookmark+newText
		except TypeError:
			text = newText
		if api.copyToClip(text):
			# Translators: message presented when the text has been appended to the clipboard.
			ui.message(_("Appended"))
		else:
			# Translators: message presented when the text cannot be appended to the clipboard.
			ui.message(_("Cannot append"))
	# Translators: message presented in input mode.
	script_append.__doc__ = _("Retrieves the selected string or the text from the previously set start marker up to and including the current position of the review cursor, and appends it to the clipboard.")

	def script_clear(self, gesture):
		self.clearClipboard()
	# Translators: message presented in input mode.
	script_clear.__doc__ = _("Deletes the appended text and the content of the clipboard.")

	__gestures = {
		"kb:NVDA+windows+c": "append",
		"kb:NVDA+windows+x": "clear",
		"kb:NVDA+windows+f9": "setSelectionStartMarker",
	}

class AddonSettingsDialog(SettingsDialog):

	# Translators: title of a dialog.
	title = _("Clip Contents Designer settings")

	def makeSettings(self, settingsSizer):
		# Translators: label of a dialog.
		setSeparatorLabel=wx.StaticText(self, -1, label=_("Type the string to be used as a &separator between contents appended to the clipboard."))
		settingsSizer.Add(setSeparatorLabel)
		self.setSeparatorEdit=wx.TextCtrl(self, wx.NewId())
		self.setSeparatorEdit.SetValue(conf["separator"]["bookmarkSeparator"])
		settingsSizer.Add(self.setSeparatorEdit, border=10, flag=wx.BOTTOM)
		# Translators: label of a dialog.
		self.copySettingsCheckBox=wx.CheckBox(self, wx.NewId(), label=_("&Copy settings"))
		self.copySettingsCheckBox.SetValue(False)
		settingsSizer.Add(self.copySettingsCheckBox,border=10, flag=wx.BOTTOM)

	def postInit(self):
		self.setSeparatorEdit.SetFocus()

	def onOk(self,evt):
		super(AddonSettingsDialog, self).onOk(evt)
		conf["separator"]["bookmarkSeparator"] = self.setSeparatorEdit.GetValue()
		global bookmark
		bookmark = getBookmark()
		try:
			conf.validate(val, copy=True)
			conf.write()
			log.info("clipContentsDesigner add-on configuration saved")
		except Exception as e:
			log.warning("Could not save clipContentsDesigner add-on configuration")
			log.debugWarning("", exc_info=True)
			raise e
		if self.copySettingsCheckBox.GetValue():
			try:
				shutil.copy(iniFileName, globalVars.appArgs.configPath)
			except:
				pass
