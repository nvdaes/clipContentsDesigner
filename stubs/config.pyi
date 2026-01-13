# config stub for NVDA add-on compatibility
from typing import Any, Sequence



from typing import Any, Sequence, Dict

class Conf:
    spec: Dict[str, Any]
    def __getitem__(self, key: str) -> Dict[str, Any]: ...
    def getConfigValidation(self, keyPath: Sequence[str]) -> 'ConfigValidationData': ...
    def save(self) -> None: ...

class ConfigValidationData:
    default: Any

conf: Conf
