# -*- coding: UTF-8 -*-
# installTasks for clipContentsDesigner add-on
#Copyright (C) 2017 Noelia Ruiz Martínez
# Released under GPL 2

import addonHandler
import gui
import wx
import config
import inputCore

addonHandler.initTranslation()

def onInstall():
	if gui.messageBox(
		# Translators: label of a dialog.
		_("This add-on allows to confirm if you want to copy to the clipboard when pressing control+c. This is named Emulate copy, and by default it works just when clipboard contains text. Do you want to configure Emulate copy now? You may do or change this later."),
		# Translators: title of a dialog.
		_("Configure Emulate copy"),
		wx.YES|wx.NO|wx.ICON_WARNING)==wx.YES:
			config.conf["clipContentsDesigner"]["confirmToCopy"] = True
			config.conf.save()
			gesture = "kb:control+c"
			module = "globalPlugins.clipContentsDesigner"
			className = "GlobalPlugin"
			scriptName = "copy"
			# Borrowed from NVDA's core.
			try:
				inputCore.manager.userGestureMap.remove(gesture, module, className, None)
			except ValueError:
				pass
			try:
				inputCore.manager.userGestureMap.remove(gesture, module, className, scriptName)
			except ValueError:
				pass
			inputCore.manager.userGestureMap.add(gesture, module, className, scriptName)
			inputCore.manager.userGestureMap.save()
