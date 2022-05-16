from typing import Any, Dict, Optional


class WXException(Exception):

    CODE = "-1"
    MESSAGE = "System Error"

    def __init__(self, code: Optional[str] = None, message: Optional[str] = None):
        super().__init__()
        self.code: str = code or self.CODE
        self.message: str = message or self.MESSAGE

    def __str__(self):
        return self.message

    def dict(self) -> Dict[str, Any]:
        return {"code": self.code, "message": self.message}
