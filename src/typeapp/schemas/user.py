from core.schemas.base import RWModel, RWBaseColumns


class UserBase(RWModel):
    username: str
    password: str
    email: str
    is_active: bool = True


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    id: int


class UserInDBBase(UserBase, RWBaseColumns):
    id: int

    class Config:
        orm_mode = True


class User(UserInDBBase):
    pass


class UserInDB(UserInDBBase):
    pass
