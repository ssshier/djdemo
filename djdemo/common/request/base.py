from typing import Any
from loguru import logger
import requests
from retry import retry

from common.constants.http import HttpMethod


class BaseRequest:
    def __init__(self) -> None:
        pass

    def get(self, url: str, **kwargs: Any) -> requests.Response:
        logger.info(f"GET {url} {kwargs}")
        return self._request(HttpMethod.GET, url, **kwargs)

    def post(self, url: str, **kwargs: Any) -> requests.Response:
        logger.info(f"POST {url} {kwargs}")
        return self._request(HttpMethod.POST, url, **kwargs)

    def put(self, url: str, **kwargs: Any) -> requests.Response:
        logger.info(f"PUT {url} {kwargs}")
        return self._request(HttpMethod.PUT, url, **kwargs)

    def delete(self, url: str, **kwargs: Any) -> requests.Response:
        logger.info(f"DELETE {url} {kwargs}")
        return self._request(HttpMethod.DELETE, url, **kwargs)

    @retry(Exception, tries=3, delay=1)
    def _request(self, method: str, url: str, **kwargs: Any) -> requests.Response:
        response = requests.request(method, url, **kwargs)
        return response
