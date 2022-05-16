from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from loguru import logger
from common.utils.token import decode_token


class LoginMiddleware(MiddlewareMixin):
    def process_request(self, request):
        token: str = request.headers.get("Authorization")
        try:
            decode_token(token)
        except Exception:
            logger.error(f"Auth fail, token: {token}")
            return JsonResponse(
                {"code": 401, "message": "Auth fail"},
                status=401,
                json_dumps_params={"ensure_ascii": False},
            )
