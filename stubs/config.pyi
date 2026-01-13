# config stub for NVDA add-on compatibility
from typing import Any, Sequence

class Conf:
	spec: dict[str, Any]
	def __getitem__(self, key: str) -> dict[str, Any]: ...
	def getConfigValidation(self, keyPath: Sequence[str]) -> "ConfigValidationData": ...
	def save(self) -> None: ...

class ConfigValidationData:
	default: Any

conf: Conf
