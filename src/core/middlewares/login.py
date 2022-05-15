from django.utils.deprecation import MiddlewareMixin


class LoginMiddleware(MiddlewareMixin):
    def process_request(self, request):

        token: str = request.COOKIES.get("Authorization")
