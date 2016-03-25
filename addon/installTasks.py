import addonHandler
import os
import shutil
import globalVars
import gui
import wx

addonHandler.initTranslation()

def onInstall():
	for addon in addonHandler.getAvailableAddons():
		if addon.manifest['name'] == "AppendText":
			if gui.messageBox(
				# Translators: the label of a message box dialog.
				_("You have installed the AppendText add-on, probably an old and incompatible version with this one. Do you want to uninstall the old version?"),
				# Translators: the title of a message box dialog.
				_("Uninstall incompatible add-on"),
				wx.YES|wx.NO|wx.ICON_WARNING)==wx.YES:
					addon.requestRemove()
			break
	if os.path.isfile(os.path.join(globalVars.appArgs.configPath, "clipContentsDesigner.ini")):
		if gui.messageBox(
			# Translators: the label of a message box dialog.
			_("You seem to have previous settings saved for this add-on. Do you want to import them?"),
			# Translators: the title of a message box dialog.
			_("Import ClipContentsDesigner add-on settings"),
			wx.YES|wx.NO|wx.ICON_WARNING)==wx.YES:
				try:
					shutil.copy(os.path.join(globalVars.appArgs.configPath, "clipContentsDesigner.ini"), os.path.join(os.path.dirname(__file__), "globalPlugins", "clipContentsDesigner"))
				except:
					pass
