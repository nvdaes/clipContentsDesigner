# Stub for scriptHandler module
from typing import Any, Callable, TypeVar

F = TypeVar('F', bound=Callable[..., Any])

def script(**kwargs: Any) -> Callable[[F], F]: ...
