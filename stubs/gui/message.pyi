# Stub for gui.message module
from typing import Any

class MessageDialog:
	@staticmethod
	def ask(
		message: Any,
		caption: str = "",
		parent: Any = None,
		yesLabel: Any = None,
		noLabel: Any = None,
		cancelLabel: Any = None,
	) -> int: ...
	@staticmethod
	def confirm(message: str, caption: str = "") -> int: ...

class ReturnCode:
	OK: int
	YES: int
	NO: int
	CANCEL: int
