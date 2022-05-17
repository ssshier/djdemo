from typing import List, Union
from pydantic import BaseModel


class PageSchema(BaseModel):
    page_num: int
    page_size: int


class FilterSchema(BaseModel):
    key: str
    value: Union[str, List]
    op: str


class SuQuerySchema(BaseModel):
    page: PageSchema
    filters: List
    sorts: List[str]
