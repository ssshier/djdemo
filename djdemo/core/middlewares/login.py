from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework.request import Request
from loguru import logger

from common.exceptions.cmm import CMMap
from common.utils.token import decode_token
from common.exceptions.wx import WXException


class LoginMiddleware(MiddlewareMixin):
    def process_request(self, request: Request):
        if request.path in ["/typeapp/login"]:
            return
        token: str = request.headers.get("Authorization")
        try:
            decode_token(token)
        except WXException as e:
            e.init(**CMMap.USER.DECODE_AUTHORIZATION_FAIL)
            logger.error(e.message)
            return JsonResponse(
                data=e.dict(), json_dumps_params={"ensure_ascii": False}
            )
