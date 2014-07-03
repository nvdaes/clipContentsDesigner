# -*- coding: UTF-8 -*-

# clipContentsDesigner: a global plugin for managing clipboard text
# Version: 1.0
# Changed menu labels according to the new add-on name
# Date: 3/07/2014

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
import win32clipboard
import wx
import gui
import os
import languageHandler
from logHandler import log
from cStringIO import StringIO
from configobj import ConfigObj
from validate import Validator


iniFileName = os.path.join(os.path.dirname(__file__), "appendText.ini")

confspec = ConfigObj(StringIO("""#Configuration file

[separator]
	bookmarkSeparator = string(default="")
"""), encoding="UTF-8", list_values=False)
confspec.newlines = "\r\n"
conf = ConfigObj(iniFileName, configspec = confspec, indent_type = "\t", encoding="UTF-8")
val = Validator()
conf.validate(val)
bookmark = conf["separator"]["bookmarkSeparator"]


addonHandler.initTranslation()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		self.menu = gui.mainFrame.sysTrayIcon.menu
		self.appendTextMenu = wx.Menu()
		self.mainItem = self.menu.AppendSubMenu(self.appendTextMenu,
		# Translators: name of a menu item.
		_("&Clip Text Manager"),
		# Translators: tooltip for a menu item.
		_("Clip Text Manager menu"))
		self.clearItem = self.appendTextMenu.Append(wx.ID_ANY,
		# Translators: name of a menu item.
		_("D&elete appended text"),
		# Translators: tooltip for a menu item.
		_("Clear clipboard and delete appended text"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onClearAddedText, self.clearItem)
		self.settingsItem = self.appendTextMenu.Append(wx.ID_ANY,
		# Translators: name of a menu item.
		_("Append Text &separator..."),
		# Translators: tooltip for a menu item.
		_("Set the separator for appended strings"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onSettings, self.settingsItem)

		self.text = ""
		self.baseText = ""
		self.newText = ""
		self.separator = "\r\n"+bookmark+"\r\n"

	def terminate(self):
		try:
			self.menu.RemoveItem(self.mainItem)
		except wx.PyDeadObjectError:
			pass

	def onSettings(self, evt):
		# Translators: label of a dialog.
		message = _("Type the text you wish to use as separator between the strings appended to clipboard")
		# Translators: title of a dialog.
		title = _("Append Text settings")
		global bookmark
		d = wx.TextEntryDialog(gui.mainFrame, message, title, defaultValue=bookmark)
		gui.mainFrame.prePopup()
		try:
			result = d.ShowModal()
		except AttributeError:
			pass
		gui.mainFrame.postPopup()
		if result == wx.ID_OK:
			bookmark = d.GetValue()
			self.separator = "\r\n"+bookmark+"\r\n"
			conf["separator"]["bookmarkSeparator"] = bookmark
			try:
				conf.validate(val, copy=True)
				conf.write()
				log.info("AppendText add-on configuration saved")
			except Exception, e:
				log.warning("Could not save AppendText add-on configuration")
				log.debugWarning("", exc_info=True)
				raise e

	def clearClipboard(self):
		try:
			win32clipboard.OpenClipboard()
			win32clipboard.EmptyClipboard()
			# ui.message(_("Clipboard is empty"))
		except win32clipboard.error:
			# Translators: message presented when cannot delete the clipboard content.
			ui.message(_("Cannot clear the clipboard"))
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
		if obj == treeInterceptor:
			try:
				clipData = api.getClipData()
			except TypeError:
				clipData = None
			try:
				info.copyToClipboard()
				selectedText = api.getClipData()
				if clipData is not None:
					api.copyToClip(clipData)
				else:
					self.clearClipboard()
				return selectedText
			except:
				pass
		return info.text

	def script_review_markStartForAppend(self, gesture):
		self._copyStartMarker = api.getReviewPosition().copy()
		# Translators: message presented when the start marker for Append Text has been set using the review cursor.
		ui.message(_("Start marked for Append Text"))
	# Translators: message presented in input mode.
	script_review_markStartForAppend.__doc__ = _("Marks the current position of the review cursor as the start of text to be appended.")

	def script_append(self, gesture):
		if self.getSelectedText() is not None:
			self.newText = self.getSelectedText()
		else:
			if not getattr(self, "_copyStartMarker", None):
				# Translators: message presented when it's not possible to append text, since no text has been selected or marked.
				ui.message(_("No selection. No start marker set"))
				return
			pos = api.getReviewPosition().copy()
			if self._copyStartMarker.obj != pos.obj:
				# Translators: message presented when trying to append text, but the start marker doesn't reside in the current object.
				ui.message(_("The start marker must reside within the same object"))
				return
			pos.move(textInfos.UNIT_CHARACTER, 1, endPoint="end")
			pos.setEndPoint(self._copyStartMarker, "startToStart")
			if not pos.compareEndPoints(pos, "startToEnd") < 0:
				# Translators: message presented when review cursor has been used to append text and there is no text to append.
				ui.message(_("No text to append"))
				return
			self.newText = textInfos.convertToCrlf(pos.text)
			self._copyStartMarker = None
		try:
			clipData = api.getClipData()
		except TypeError:
			clipData = ""
			# Translators: message presented when adding text to the clipboard and it's empty.
			ui.message(_("Adding text to empty clipboard"))
		try:
			self.baseText = clipData+self.separator
			self.text = self.baseText+self.newText
		except Exception, e:
			# Translators: message presented when the text to append cannot be retrieved.
			ui.message(_("Can not get the text to append"))
			raise e
		if api.copyToClip(self.text):
			# Translators: message presented when the text has been appended to the clipboard.
			ui.message(_("Appended"))
		else:
			# Translators: message presented when the text cannot be apended to the clipboard.
			ui.message(_("Cannot append text to the clipboard"))
	# Translators: message presented in input mode.
	script_append.__doc__ = _("Retrieves the selected string or the text from the previously set start marker up to and including the current position of the review cursor, and appends it to the clipboard.")

	def onClearAddedText(self, evt):
		# Translators: message presented when deleting the clipboard content.
		ui.message(_("Clearing added text..."))
		self.text = ""
		self.baseText = ""
		self.newText = ""
		self.clearClipboard()
		try:
			api.getClipData()
		except TypeError:
			# Translators: message presented when the clipboard content has been deleted.
			ui.message(_("Clipboard is empty"))

	def script_clear(self, gesture):
		self.onClearAddedText(None)
	# Translators: message presented in input mode.
	script_clear.__doc__ = _("Deletes the appended text and the content of the clipboard.")

	__gestures = {
		"kb:control+NVDA+shift+e": "append",
		"kb:control+NVDA+shift+x": "clear",
		"kb:control+NVDA+shift+c": "review_markStartForAppend",
	}
