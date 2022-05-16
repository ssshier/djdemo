from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework.request import Request
from common.exceptions.wx import WXException


class ExceptionMiddleware(MiddlewareMixin):
    def process_exception(self, _: Request, exception: Exception):
        if isinstance(exception, WXException):
            return JsonResponse(
                data=exception.dict(), json_dumps_params={"ensure_ascii": False}
            )
        message = exception.args
        result = WXException(message=str(message)).dict()
        return JsonResponse(
            data=result, status=500, json_dumps_params={"ensure_ascii": False}
        )
