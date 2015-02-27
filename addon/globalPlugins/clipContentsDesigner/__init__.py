# -*- coding: UTF-8 -*-

# clipContentsDesigner: a global plugin for managing clipboard text
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
import wx
import gui
import os
import codecs
from logHandler import log

addonHandler.initTranslation()

try:
	from globalCommands import SCRCAT_TEXTREVIEW
except:
	SCRCAT_TEXTREVIEW = None

<<<<<<< HEAD
=======
iniFileName = os.path.join(os.path.dirname(__file__), "clipContentsDesigner.ini")

confspec = ConfigObj(StringIO("""#Configuration file

[separator]
	bookmarkSeparator = string(default="")
"""), encoding="UTF-8")
confspec.newlines = "\r\n"
conf = ConfigObj(iniFileName, configspec = confspec, indent_type = "\t", encoding="UTF-8")
val = Validator()
conf.validate(val)


>>>>>>> hindi
class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	scriptCategory = SCRCAT_TEXTREVIEW

	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		self.prefsMenu = gui.mainFrame.sysTrayIcon.preferencesMenu
		self.settingsItem = self.prefsMenu.Append(wx.ID_ANY,
			# Translators: name of the option in the menu.
			_("Set &Clip Contents Designer separator"),
			"")
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onSettings, self.settingsItem)

		self._copyStartMarker = None
<<<<<<< HEAD
		self.separatorFile = os.path.join(os.path.dirname(__file__), "clipContentsDesigner.txt")
=======
		self.bookmark = "\r\n%s\r\n" % conf["separator"]["bookmarkSeparator"]
>>>>>>> hindi

	def terminate(self):
		try:
			self.prefsMenu.RemoveItem(self.settingsItem)
		except wx.PyDeadObjectError:
			pass

<<<<<<< HEAD
	def getSeparator(self):
		try:
			with codecs.open(self.separatorFile, "r", "utf-8") as f:
				bookmark = f.read()
		except:
			bookmark = "\r\n\r\n"
		return bookmark

	def onSettings(self, evt):
		if not os.path.isfile(self.separatorFile):
=======
	def onSettings(self, evt):
		# Translators: label of a dialog.
		message = _("Type the string to be used as a separator between contents appended to the clipboard.")
		# Translators: title of a dialog.
		title = _("Clip Contents Designer settings")
		d = wx.TextEntryDialog(gui.mainFrame, message, title, defaultValue=conf["separator"]["bookmarkSeparator"])
		gui.mainFrame.prePopup()
		try:
			result = d.ShowModal()
		except AttributeError:
			pass
		gui.mainFrame.postPopup()
		if result == wx.ID_OK:
			conf["separator"]["bookmarkSeparator"] = d.GetValue()
			self.bookmark = "\r\n%s\r\n" % conf["separator"]["bookmarkSeparator"]
>>>>>>> hindi
			try:
				with codecs.open(self.separatorFile, "w", "utf-8") as f:
					f.write("\r\n\r\n")
			except Exception, e:
				log.debugWarning("Error writing separator for clipContentsDesigner", exc_info=True)
				raise e
		try:
			os.startfile(self.separatorFile)
		except:
			pass

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

	def script_setSelectionStartMarker(self, gesture):
		self._copyStartMarker = api.getReviewPosition().copy()
		# Translators: message presented when the start marker for appending text has been set using the review cursor.
		ui.message(_("Start marker set"))
	# Translators: message presented in input mode.
	script_setSelectionStartMarker.__doc__ = _("Marks the current position of the review cursor as the start of text to be appended to the clipboard.")

	def script_append(self, gesture):
		newText = self.getSelectedText()
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
<<<<<<< HEAD
			text = clipData+self.getSeparator()+newText
=======
			text = clipData+self.bookmark+newText
>>>>>>> hindi
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
