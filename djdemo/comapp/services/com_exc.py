from typing import Any, Dict, List
from comapp.mappers.com_exc import com_exc_mapper
from comapp.models.com_exc import ComExc
from comapp.schemas.com_exc import ComExc as ComExcSchema
from comapp.schemas.com_exc import ComExcCreate, ComExcUpdate
from core.services.base import BaseService


class ComExcService(BaseService):
    def __init__(self):
        super().__init__()
        self.mapper = com_exc_mapper

    def list(self) -> List[Dict[str, Any]]:
        objs = self.mapper.list()
        return [ComExcSchema.from_orm(obj).dict() for obj in objs]

    def get(self, pk: int) -> Dict[str, Any]:
        obj = self.mapper.get(pk)
        return ComExcSchema.from_orm(obj).dict()

    def create(self, obj_in: ComExcCreate) -> Dict[str, Any]:
        obj = self.mapper.create(obj_in)
        return ComExcSchema.from_orm(obj).dict()

    def update(self, obj_in: ComExcUpdate) -> Dict[str, Any]:
        db_obj: ComExc = self.mapper.get(obj_in.id)
        obj = self.mapper.update(db_obj, obj_in)
        return ComExcSchema.from_orm(obj).dict()

    def delete(self, pk: int) -> int:
        pk = self.mapper.remove(pk)
        return pk
