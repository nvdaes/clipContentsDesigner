# -*- coding: UTF-8 -*-
#A simple module to bypass the addon translation system,
#so it can take advantage from the NVDA translations directly.
import ui

def message(message):
	ui.message(_(message))
