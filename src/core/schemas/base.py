from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class RWModel(BaseModel):
    class Config:
        json_encoders = {
            datetime: repr
        }


class RWBaseColumns(BaseModel):
    id: Optional[int]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    created_by: Optional[str]
    updated_by: Optional[str]
    is_deleted: Optional[bool]

    class Config:
        json_encoders = {
            datetime: repr
        }
