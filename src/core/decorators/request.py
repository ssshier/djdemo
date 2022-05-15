import functools
from typing import Any, List

from rest_framework.request import Request


def require_http_methods(methods: List[str]):
    def decorator(func: Any):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any):
            if len(args) == 1:
                request: Request = args[0]
            else:
                request: Request = args[1]
            if request.method not in methods:
                raise Exception("Method not allowed")
            return func(*args, **kwargs)

        return wrapper

    return decorator
