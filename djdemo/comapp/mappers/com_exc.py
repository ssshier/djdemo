from comapp.models.com_exc import ComExc
from comapp.schemas.com_exc import ComExcCreate, ComExcUpdate
from core.mappers.base import BaseMapper


class ComExcMapper(BaseMapper[ComExc, ComExcCreate, ComExcUpdate]):
    pass


com_exc_mapper = ComExcMapper(ComExc)
