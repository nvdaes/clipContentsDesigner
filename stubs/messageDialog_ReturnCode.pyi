# Expanded stub for MessageDialog and ReturnCode
from typing import Any

class MessageDialog:
	@staticmethod
	def ask(
		message: str,
		caption: str = "",
		parent: Any = None,
		yesLabel: Any = None,
		noLabel: Any = None,
		cancelLabel: Any = None,
	) -> "ReturnCode": ...
	@staticmethod
	def confirm(message: str, caption: str = "") -> "ReturnCode": ...

class ReturnCode:
	OK: int
	YES: int
	NO: int
	CANCEL: int
