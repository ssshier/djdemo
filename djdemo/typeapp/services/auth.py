from django.contrib.auth.hashers import check_password

from common.utils.token import encode_token
from typeapp.mappers.user import user_mapper
from typeapp.models.user import User
from typeapp.schemas.auth import LoginSchema


class LoginService:
    def __init__(self):
        self.mapper = user_mapper

    def login(self, obj_in: LoginSchema):
        obj: User = self.mapper.get_by_username(obj_in.username)
        if check_password(obj_in.password, obj.password):
            return encode_token(obj.username)
        raise ValueError("Login failed")
