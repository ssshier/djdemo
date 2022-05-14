from typing import Any, Dict, List
from typeapp.mappers.user import user_mapper
from typeapp.models.user import User
from typeapp.schemas.user import User as UserSchema
from typeapp.schemas.user import UserCreate, UserUpdate
from core.services.base import BaseService


class UserService(BaseService):

    def __init__(self):
        super().__init__()
        self.mapper = user_mapper

    def list(self) -> List[Dict[str, Any]]:
        objs = self.mapper.list()
        return [UserSchema.from_orm(obj).dict() for obj in objs]

    def get(self, pk: int) -> Dict[str, Any]:
        obj = self.mapper.get(pk)
        return UserSchema.from_orm(obj).dict()

    def create(self, obj_in: UserCreate) -> Dict[str, Any]:
        obj = self.mapper.create(obj_in)
        return UserSchema.from_orm(obj).dict()

    def update(self, obj_in: UserUpdate) -> Dict[str, Any]:
        db_obj: User = self.mapper.get(obj_in.id)
        obj = self.mapper.update(db_obj, obj_in)
        return UserSchema.from_orm(obj).dict()

    def delete(self, pk: int) -> int:
        pk = self.mapper.remove(pk)
        return pk

    def get_by_username(self, username: str) -> Dict[str, Any]:
        obj = self.mapper.get_by_username(username)
        return UserSchema.from_orm(obj).dict()

    def get_by_email(self, email: str) -> Dict[str, Any]:
        obj = self.mapper.get_by_email(email)
        return UserSchema.from_orm(obj).dict()