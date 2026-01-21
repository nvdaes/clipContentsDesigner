# Stub for mathPres module
from typing import Any

def getMathMlFromTextInfo(textInfo: Any) -> str | None: ...

class BrailleProvider:
	def getBrailleForMathMl(__self, __mathMl: str, /) -> str: ...

brailleProvider: BrailleProvider | None
