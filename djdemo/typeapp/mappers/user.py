from typeapp.models.user import User
from typeapp.schemas.user import UserCreate, UserPasswordChange, UserUpdate
from core.mappers.base import BaseMapper


class UserMapper(BaseMapper[User, UserCreate, UserUpdate]):
    def get_by_username(self, username: str) -> User:
        return self.model.objects.get(username=username)

    def get_by_email(self, email: str) -> User:
        return self.model.objects.get(email=email)

    def change_password(self, obj_in: UserPasswordChange):
        db_obj: User = self.model.objects.get(username=obj_in.username)
        db_obj.password = obj_in.password
        db_obj.save()
        return db_obj


user_mapper = UserMapper(User)
