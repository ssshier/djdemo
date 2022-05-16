import functools
import time
from typing import Any

from loguru import logger


def timer() -> Any:
    def decorate(func: Any) -> Any:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start = time.time()
            result: Any = func(*args, **kwargs)
            end = time.time()
            logger.info("{} took {} seconds".format(func.__name__, end - start))
            return result

        return wrapper

    return decorate
