from rest_framework.views import APIView  # type: ignore

from typeapp.services.user import UserService
from typeapp.schemas.user import UserCreate, UserUpdate
from typeapp.utils.response import response_decorator


class UserView(APIView):

    def __init__(self) -> None:
        super().__init__()
        self.service = UserService()

    @response_decorator
    def list(self, request):
        return self.service.list()

    @response_decorator
    def get(self, request):
        pk = request.GET.get("id")
        return self.service.get(pk)

    @response_decorator
    def post(self, request):
        user = UserCreate(**request.data)
        return self.service.create(user)

    @response_decorator
    def put(self, request):
        user = UserUpdate(**request.data)
        return self.service.update(user)

    @response_decorator
    def delete(self, request):
        pk = request.GET.get("id")
        return self.service.delete(pk)
