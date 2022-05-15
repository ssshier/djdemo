from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

from common.utils.token import decode_token


class LoginMiddleware(MiddlewareMixin):
    def process_request(self, request):
        token: str = request.headers.get("Authorization")
        try:
            decode_token(token)
        except Exception:
            return JsonResponse(
                {"code": 401, "message": "auth failed"},
                status=401,
                json_dumps_params={"ensure_ascii": False},
            )
