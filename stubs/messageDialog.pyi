# Stub for MessageDialog.ask and ReturnCode
from typing import Any

class MessageDialog:
    @staticmethod
    def ask(message: Any, caption: str = '', parent: Any = None, yesLabel: Any = None, noLabel: Any = None, cancelLabel: Any = None) -> 'ReturnCode': ...
    @staticmethod
    def confirm(__message: str, __caption: str = '', /) -> 'ReturnCode': ...

class ReturnCode:
    OK: int
    YES: int
    NO: int
    CANCEL: int
