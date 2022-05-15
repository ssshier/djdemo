from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin


class ExceptionMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        message = exception.args
        result = {"code": 500, "message": message}
        return JsonResponse(
            data=result, status=500, json_dumps_params={"ensure_ascii": False}
        )
