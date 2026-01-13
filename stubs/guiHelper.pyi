# guiHelper stub for NVDA add-on compatibility

from typing import Any, TypeVar

_T = TypeVar("_T")

class BoxSizerHelper:
	def __init__(self, parent: Any, sizer: Any = None) -> None: ...
	def addLabeledControl(self, labelText: str, wxCtrlClass: type[_T], **kwargs: Any) -> _T: ...
	def addItem(self, item: _T, **keywordArgs: Any) -> _T: ...
