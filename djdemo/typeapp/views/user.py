from django.views.decorators.http import require_http_methods
from rest_framework.views import APIView  # type: ignore
from rest_framework.request import Request  # type: ignore

from typeapp.services.user import UserService
from typeapp.schemas.user import UserCreate, UserUpdate, UserPasswordChange
from typeapp.utils.response import response_decorator


class UserView(APIView):
    def __init__(self) -> None:
        super().__init__()
        self.service = UserService()

    @response_decorator
    def list(self, _):
        return self.service.list()

    @response_decorator
    def get(self, request: Request):
        pk = request.GET.get("id")
        return self.service.get(pk)

    @response_decorator
    def post(self, request: Request):
        user = UserCreate(**request.data)
        return self.service.create(user)

    @response_decorator
    def put(self, request: Request):
        user = UserUpdate(**request.data)
        return self.service.update(user)

    @response_decorator
    def delete(self, request: Request):
        pk = request.GET.get("id")
        return self.service.delete(pk)

    @require_http_methods(["GET"])
    @response_decorator
    def get_by_username(self, request: Request):
        username = request.GET.get("username")
        return self.service.get_by_username(username)

    @require_http_methods(["GET"])
    @response_decorator
    def get_by_email(self, request: Request):
        email = request.GET.get("email")
        return self.service.get_by_email(email)

    @require_http_methods(["POST"])
    @response_decorator
    def change_password(self, request: Request):
        obj_in = UserPasswordChange(**request.data)
        return self.service.change_password(obj_in)


class UserByUsernameView(APIView):
    def __init__(self) -> None:
        super().__init__()
        self.service = UserService()

    @response_decorator
    def get(self, request: Request):
        username = request.GET.get("username")
        return self.service.get_by_username(username)


class UserByEmailView(APIView):
    def __init__(self) -> None:
        super().__init__()
        self.service = UserService()

    @response_decorator
    def get(self, request: Request):
        email = request.GET.get("email")
        return self.service.get_by_email(email)


class UserPasswordChangeView(APIView):
    def __init__(self) -> None:
        super().__init__()
        self.service = UserService()

    @response_decorator
    def post(self, request: Request):
        obj_in = UserPasswordChange(**request.data)
        return self.service.change_password(obj_in)
