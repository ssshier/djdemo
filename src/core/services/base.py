from typing import Any


class BaseService:
    def __init__(self):
        pass

    def list(self) -> Any:
        pass
    
    def page(self) -> Any:
        pass

    def get(self, pk: int) -> Any:
        pass

    def create(self, obj_in: Any) -> Any:
        pass

    def update(self, obj_in: Any) -> Any:
        pass

    def delete(self, pk: int) -> Any:
        pass
