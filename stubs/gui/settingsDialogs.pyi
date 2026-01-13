# Stub for gui.settingsDialogs module
from typing import Any

class SettingsPanel:
	def __init__(self, parent: Any) -> None: ...
	def makeSettings(self, sizer: Any) -> None: ...
	def onSave(self) -> None: ...

class NVDASettingsDialog:
	categoryClasses: list[type[SettingsPanel]]
