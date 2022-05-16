import functools
from typing import Any

from django.http import JsonResponse
from loguru import logger


def response_decorator(func: Any):
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any):
        try:
            data = func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Request exception, detail: {e}")
            message = e.args
            result = {"code": 500, "message": message}
            return JsonResponse(
                data=result, status=500, json_dumps_params={"ensure_ascii": False}
            )
        result = {"code": 200, "data": data, "message": "success"}
        return JsonResponse(data=result, json_dumps_params={"ensure_ascii": False})

    return wrapper
