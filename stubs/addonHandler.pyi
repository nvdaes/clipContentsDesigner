# Expanded stub for addonHandler
from typing import Any, Dict

class Addon:
    manifest: Dict[str, Any]

def initTranslation() -> None: ...
def getCodeAddon() -> Addon: ...
