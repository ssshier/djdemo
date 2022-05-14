from typing import Any, Dict, List
from typeapp.dao.user import user_dao
from typeapp.models.user import User
from typeapp.schemas.user import User as UserSchema
from typeapp.schemas.user import UserCreate, UserUpdate
from core.services.base import BaseService


class UserService(BaseService):

    def __init__(self):
        super().__init__()
        self.dao = user_dao

    def list(self) -> List[Dict[str, Any]]:
        objs = self.dao.list()
        return [UserSchema.from_orm(obj).dict() for obj in objs]

    def get(self, pk: int) -> Dict[str, Any]:
        obj = self.dao.get(pk)
        return UserSchema.from_orm(obj).dict()

    def create(self, obj_in: UserCreate) -> Dict[str, Any]:
        obj = self.dao.create(obj_in)
        return UserSchema.from_orm(obj).dict()

    def update(self, obj_in: UserUpdate) -> Dict[str, Any]:
        db_obj: User = self.dao.get(obj_in.id)
        obj = self.dao.update(db_obj, obj_in)
        return UserSchema.from_orm(obj).dict()

    def delete(self, pk: int) -> int:
        pk = self.dao.remove(pk)
        return pk
