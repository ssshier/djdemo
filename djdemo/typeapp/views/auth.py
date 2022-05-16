from rest_framework.views import APIView
from rest_framework.request import Request

from typeapp.schemas.auth import LoginSchema
from typeapp.services.auth import LoginService
from core.decorators.response import response_decorator


class LoginView(APIView):
    def __init__(self):
        super(LoginView, self).__init__()
        self.service = LoginService()

    @response_decorator
    def post(self, request: Request):
        obj_in = LoginSchema(**request.data)
        return self.service.login(obj_in)
