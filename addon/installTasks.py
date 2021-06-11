# -*- coding: UTF-8 -*-
# installTasks for clipContentsDesigner add-on
# Copyright (C) 2017-2018 Noelia Ruiz Martínez
# Released under GPL 2

import addonHandler
import gui
import wx
import inputCore
import config

addonHandler.initTranslation()

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


def onInstall():
	module = "globalPlugins.clipContentsDesigner"
	className = "GlobalPlugin"
	copyGesture = "kb:control+c"
	copyScriptName = "copy"
	cutGesture = "kb:control+x"
	cutScriptName = "cut"
	try:
		inputCore.manager.userGestureMap.remove(copyGesture, module, className, copyScriptName)
		inputCore.manager.userGestureMap.remove(cutGesture, module, className, cutScriptName)
	except ValueError:
		pass
	if gui.messageBox(
		# Translators: label of a dialog.
		_("""This add-on allows to confirm if you want to copy and cut, replacing the clipboard contents,
		when pressing control+c and control+x. This is named Emulate copy and cut.
		Do you want to configure Emulate copy and cut now? You may do or change this later."""),
		# Translators: title of a dialog.
		_("Configure Emulate copy and cut"),
		wx.YES | wx.NO | wx.ICON_WARNING
	) == wx.YES:
		config.conf.spec["clipContentsDesigner"] = confspec
		config.conf["clipContentsDesigner"]["confirmToCopy"] = True
		config.conf["clipContentsDesigner"]["confirmToCut"] = True
		config.conf.save()
		# Adapted from NVDA's core.
		inputCore.manager.userGestureMap.add(copyGesture, module, className, copyScriptName)
		inputCore.manager.userGestureMap.add(cutGesture, module, className, cutScriptName)
	inputCore.manager.userGestureMap.save()
