from typing import Any, Dict, Optional


class WXException(Exception):
    CODE = "-1"
    MESSAGE = "System Error"

    def __init__(
        self, code: Optional[str] = None, message: Optional[str] = None, **kwargs: Any
    ):
        super().__init__()
        self._init(code, message, **kwargs)

    def __str__(self):
        return self.message

    def init(
        self, code: Optional[str] = None, message: Optional[str] = None, **kwargs: Any
    ):
        self._init(code, message, **kwargs)

    def dict(self) -> Dict[str, Any]:
        return {"code": self.code, "message": self.message}

    def _init(
        self, code: Optional[str] = None, message: Optional[str] = None, **kwargs: Any
    ):
        self.code: str = code or self.CODE
        self.message: str = message or self.MESSAGE
