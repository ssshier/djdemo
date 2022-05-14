from typeapp.models.user import User
from typeapp.schemas.user import UserCreate, UserUpdate
from core.dao.base import BaseDao


class UserDao(BaseDao[User, UserCreate, UserUpdate]):
    
    pass

user_dao = UserDao(User)
