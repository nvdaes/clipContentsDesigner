# Expanded stub for addonHandler
from typing import Any

class Addon:
    manifest: dict[str, Any]

def initTranslation() -> None: ...
def getCodeAddon() -> Addon: ...
