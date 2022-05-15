from pydantic import validator  # type: ignore
from django.contrib.auth.hashers import make_password
from core.schemas.base import RWModel, RWBaseColumns


class UserBase(RWModel):
    username: str
    email: str
    is_active: bool = True


class UserCreate(UserBase):
    password: str

    @validator("password")
    def validate_password(cls, v: str):
        return make_password(v)


class UserUpdate(UserBase):
    id: int


class UserPasswordChange(RWModel):
    username: str
    password: str
    password_confirm: str


class UserInDBBase(UserBase, RWBaseColumns):
    id: int

    class Config:
        orm_mode = True


class User(UserInDBBase):
    pass


class UserInDB(UserInDBBase):
    pass
