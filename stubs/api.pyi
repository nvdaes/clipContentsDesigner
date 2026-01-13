# Stub for api module
from typing import Any

class NVDAObject:
    treeInterceptor: Any
    mathMl: str
    role: Any
    _selectThenCopyRange: Any
    def makeTextInfo(__self, __position: str, /) -> Any: ...

class TextInfo:
    clipboardText: str
    isCollapsed: bool
    obj: NVDAObject

def getFocusObject() -> NVDAObject: ...
def getNavigatorObject() -> NVDAObject: ...
def getReviewPosition() -> TextInfo: ...
def copyToClip(text: str) -> bool: ...
def getClipData() -> str: ...
