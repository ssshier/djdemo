from typeapp.models.user import User
from typeapp.schemas.user import UserCreate, UserUpdate
from core.dao.base import BaseDao


class UserDao(BaseDao[User, UserCreate, UserUpdate]):
    pass

    def get_by_username(self, username: str) -> User:
        return self.model.objects.get(username=username)
    
    def get_by_email(self, email: str) -> User:
        return self.model.objects.get(email=email)

user_dao = UserDao(User)
