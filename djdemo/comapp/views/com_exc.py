from rest_framework.views import APIView
from rest_framework.request import Request

from comapp.services.com_exc import ComExcService
from comapp.schemas.com_exc import ComExcCreate, ComExcUpdate
from core.decorators.response import response_decorator


class ComExcView(APIView):
    def __init__(self) -> None:
        super().__init__()
        self.service = ComExcService()

    @response_decorator
    def list(self, _):
        return self.service.list()

    @response_decorator
    def get(self, request: Request):
        pk = request.GET.get("id")
        return self.service.get(pk)

    @response_decorator
    def post(self, request: Request):
        com_exc = ComExcCreate(**request.data)
        return self.service.create(com_exc)

    @response_decorator
    def put(self, request: Request):
        com_exc = ComExcUpdate(**request.data)
        return self.service.update(com_exc)

    @response_decorator
    def delete(self, request: Request):
        pk = request.GET.get("id")
        return self.service.delete(pk)
