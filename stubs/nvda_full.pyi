# Expanded stub for NVDA add-on development
from typing import Any, Callable, Sequence

# Translation function
_: Callable[[str], str]

# wxPython stubs
class wx:
	TextCtrl: Any
	CheckBox: Any
	Button: Any
	Choice: Any
	EVT_BUTTON: Any
	@staticmethod
	def CallAfter(func: Callable[..., Any], *args: Any, **kwargs: Any) -> None: ...
	MessageBoxCaptionStr: str
	@staticmethod
	def MessageBox(message: str, caption: str | None = None, style: int | None = None) -> int: ...

# gui stubs
class gui:
	class nvdaControls:
		class CustomCheckListBox:
			CheckedItems: list[int]
			def IsChecked(self, index: int) -> bool: ...
			def Select(self, index: int) -> None: ...

		class SelectOnFocusSpinCtrl:
			def GetValue(self) -> int: ...
			def SetValue(self, value: int) -> None: ...

	class mainFrame:
		Handle: Any
		@staticmethod
		def popupSettingsDialog(dialogClass: Any, panelClass: Any) -> None: ...

	class blockAction:
		class Context:
			MODAL_DIALOG_OPEN: Any

		@staticmethod
		def when(context: Any) -> Callable[..., Any]: ...

class guiHelper:
	class BoxSizerHelper:
		def __init__(self, parent: Any, sizer: Any = None) -> None: ...
		def addLabeledControl(self, labelText: str, wxCtrlClass: Any, **kwargs: Any) -> Any: ...
		def addItem(self, item: Any, **keywordArgs: Any) -> Any: ...

# Settings dialogs
class SettingsPanel: ...

class NVDASettingsDialog:
	categoryClasses: list[Any]

# Message dialog
class MessageDialog:
	@staticmethod
	def confirm(message: str, caption: str | None = None) -> "ReturnCode": ...
	@staticmethod
	def ask(message: str, caption: str | None = None) -> "ReturnCode": ...

class ReturnCode:
	OK: int
	YES: int
	NO: int
	CANCEL: int

# Keyboard input
class KeyboardInputGesture:
	@staticmethod
	def fromName(name: str) -> "KeyboardInputGesture": ...
	def send(self) -> None: ...

# Addon handler
class addonHandler:
	@staticmethod
	def initTranslation() -> None: ...
	@staticmethod
	def getCodeAddon() -> Any: ...

# Config
class config:
	class conf:
		spec: dict[str, Any]
		def __getitem__(self, key: str) -> dict[str, Any]: ...
		def getConfigValidation(self, keyPath: Sequence[str]) -> Any: ...
		def save(self) -> None: ...

# Input core
class inputCore:
	class manager:
		class userGestureMap:
			@staticmethod
			def add(gesture: str, module: str, className: str, scriptName: str) -> None: ...
			@staticmethod
			def remove(gesture: str, module: str, className: str, scriptName: str) -> None: ...
			@staticmethod
			def save() -> None: ...

# API, textInfos, controlTypes, ui, winUser, browseMode, core, logHandler, locale
api: Any
textInfos: Any
controlTypes: Any
ui: Any
winUser: Any
browseMode: Any
core: Any
logHandler: Any
locale: Any
browseableMessage: Any
mathPres: Any
scriptHandler: Any
globalPluginHandler: Any
globalVars: Any

# Common attributes for settings panel
class AddonSettingsPanel(SettingsPanel):
	setSeparatorEdit: Any
	addTextBeforeCheckBox: Any
	confirmList: Any
	confirmRequirementChoices: Any
	formatChoices: Any
	maxLengthEdit: Any
	runOnInstallCheckBox: Any
	restoreDefaultsButton: Any
	def onRestoreDefaults(self, evt: Any) -> None: ...
	def onSave(self) -> None: ...

# Variables from buildVars.py
confspec: dict[str, Any]
addon_info: dict[str, Any]
pythonSources: list[str]
i18nSources: list[str]
excludedFiles: list[str]
baseLanguage: str
markdownExtensions: list[str]

# Other common types
AnyType: Any
