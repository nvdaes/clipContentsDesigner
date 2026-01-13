# Expanded stub for config.conf
from typing import Any, Sequence

class conf:
    spec: dict[str, Any]
    def __getitem__(self, key: str) -> dict[str, Any]: ...
    def getConfigValidation(self, keyPath: Sequence[str]) -> 'ConfigValidationData': ...
    def save(self) -> None: ...

class ConfigValidationData:
    default: Any
