from core.schemas.base import RWModel, RWBaseColumns


class ComExcBase(RWModel):
    app_code: str
    app_name: str
    module_code: str
    module_name: str
    name: str
    code: str
    message: str


class ComExcCreate(ComExcBase):
    pass


class ComExcUpdate(ComExcBase):
    id: int


class ComExcInDBBase(ComExcBase, RWBaseColumns):
    id: int

    class Config:
        orm_mode = True


class ComExc(ComExcInDBBase):
    pass


class ComExcInDB(ComExcInDBBase):
    pass
