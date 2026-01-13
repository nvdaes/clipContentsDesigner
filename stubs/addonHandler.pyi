# Expanded stub for addonHandler
from typing import Any, Dict

class Addon:
    manifest: Dict[str, Any]

def getCodeAddon() -> Addon: ...

class addonHandler:
    @staticmethod
    def initTranslation() -> None: ...
    @staticmethod
    def getCodeAddon() -> Addon: ...
