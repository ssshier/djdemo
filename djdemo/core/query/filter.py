from typing import Any, Dict, List, Type
from django.db.models import Model
from django.db.models import QuerySet


class Filter:
    def __init__(self, model: Type[Model], query: QuerySet, filters: List[Any]):
        self.model = model
        self.query = query
        self.filters = filters

    def filter(self) -> QuerySet:
        condition_maps: Dict[str, Any] = {}
        for _filter in self.filters:
            condition = self._condition(_filter)
            condition_maps.update(condition)
        self.query = self.query.filter(**condition_maps)
        return self.query

    def _condition(self, _filter: Dict[str, Any]) -> Dict[str, Any]:
        op = _filter.get("op")
        key = _filter.get("key")
        value = _filter.get("value")
        if not op or not hasattr(self.model, key):
            return {}
        if op == "eq":
            return {key: value}
        else:
            return {key + op: value}
