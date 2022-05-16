import datetime
from typing import Any, Dict
import jwt
from loguru import logger
from common.exceptions.wx import WXException


def encode_token(data: str) -> str:
    payload = {
        "data": data,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7),
    }
    return jwt.encode(payload, "secret", algorithm="HS256")


def decode_token(encoded: str) -> str:
    try:
        payload: Dict[str, Any] = jwt.decode(encoded, "secret", algorithms=["HS256"])
        return payload["data"]
    except jwt.exceptions.DecodeError as e:
        logger.error(e.args)
    raise WXException()
