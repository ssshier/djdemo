from typing import Any, Dict, Generic, Type, TypeVar, Union

from django.db.models import Model
from django.forms import model_to_dict
from pydantic import BaseModel

from core.query.filter import Filter
from core.query.page import Page
from core.query.sort import Sort
from core.schemas.query import SuQuerySchema

ModelType = TypeVar("ModelType", bound=Model)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseMapper(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]) -> None:
        self.model = model

    def list(self) -> Any:
        return self.model.objects.all()

    def query(self, obj_in: SuQuerySchema) -> Any:
        q = Filter(self.model, self.model.objects, obj_in.filters).filter()
        s = Sort(q, obj_in.sorts).sort()
        p = Page(s, obj_in.page)
        return p.dict()

    def get(self, id: Any):
        return self.model.objects.get(id=id)

    def create(self, obj_in: CreateSchemaType) -> ModelType:
        obj: ModelType = self.model(**obj_in.dict())
        obj.save()
        return obj

    def update(
        self, db_obj: ModelType, obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        obj_data = model_to_dict(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db_obj.save()
        return db_obj

    def remove(self, pk: Any) -> int:
        obj = self.model.objects.get(id=pk)
        obj.delete()
        return pk
