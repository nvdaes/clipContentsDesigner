# Expanded stub for inputCore.manager and userGestureMap
from typing import Any

class userGestureMap:
    def add(self, gesture: str, module: str, className: str, scriptName: str) -> None: ...
    def remove(self, gesture: str, module: str, className: str, scriptName: str) -> None: ...
    def save(self) -> None: ...

class manager:
    userGestureMap: userGestureMap
