from typing import Any
import requests # type: ignore
from retry import retry # type: ignore

from common.constants.http import HttpMethod

class BaseRequest:

    def __init__(self) -> None:
        pass

    def get(self, url: str, **kwargs: Any) -> requests.Response:
        return self._request(HttpMethod.GET, url, **kwargs)

    def post(self, url: str, **kwargs: Any) -> requests.Response:
        return self._request(HttpMethod.POST, url, **kwargs)

    def put(self, url: str, **kwargs: Any) -> requests.Response:
        return self._request(HttpMethod.PUT, url, **kwargs)

    def delete(self, url: str, **kwargs: Any) -> requests.Response:
        return self._request(HttpMethod.DELETE, url, **kwargs)

    @retry(Exception, tries=3, delay=1)
    def _request(self, method: str, url: str, **kwargs: Any) -> requests.Response:
        response = requests.request(method, url, **kwargs)
        return response
