# -*- coding: UTF-8 -*-
import os.path
# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

# Full getext (please don't change)
_ = lambda x: x

# Add-on information variables
addon_info = {
	# for previously unpublished addons, please follow the community guidelines at:
	# https://bitbucket.org/nvdaaddonteam/todo/raw/master/guideLines.txt
	# add-on Name, internal for nvda
	"addon_name": "clipContentsDesigner",
	# Add-on summary, usually the user visible name of the addon.
	# Translators: Summary for this add-on to be shown on installation and add-on information.
	"addon_summary": _("Clip Contents Designer"),
	# Add-on description
	"addon_description": _(
		# Translators: Long description to be shown for this add-on on add-on information from add-ons manager
		"""Allows the joining of separate fragments of text on the clipboard and clearing of clipboard content. Current text on the clipboard can be presented in browse mode. Option to request confirmation before performing actions such as copy, cut, add text, or clearing the clipboard to avoid accidental changes.""",
	),
	# version
	"addon_version": "48.1.0",
	# Author(s)
	"addon_author": "Noelia <nrm1977@gmail.com>, Abdel <abdelkrim.bensaid@gmail.com>",
	# URL for the add-on documentation support
	"addon_url": "https://github.com/nvdaes/clipContentsDesigner",
	# Documentation file name
	"addon_docFileName": "readme.html",
	# Minimum NVDA version supported (e.g. "2018.3")
	"addon_minimumNVDAVersion": "2025.1",
	# Last NVDA version supported/tested (e.g. "2018.4", ideally more recent than minimum version)
	"addon_lastTestedNVDAVersion": "2025.2.0",
	# Add-on update channel (default is stable or None)
	"addon_updateChannel": None,
}


# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = [
	os.path.join("addon", "*.py"),
	os.path.join("addon", "globalPlugins", "clipContentsDesigner", "*.py"),
]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = []

# Base language for the NVDA add-on
# If your add-on is written in a language other than english, modify this variable.
# For example, set baseLanguage to "es" if your add-on is primarily written in spanish.
baseLanguage = "en"

# Markdown extensions for add-on documentation
# Most add-ons do not require additional Markdown extensions.
# If you need to add support for markup such as tables, fill out the below list.
# Extensions string must be of the form "markdown.extensions.extensionName"
# e.g. "markdown.extensions.tables" to add tables.
markdownExtensions = []
