from typing import List

from django.db.models.query import QuerySet


class Sort:
    def __init__(self, query: QuerySet, fields: List[str]) -> None:
        self.query = query
        self.fields = fields

    def sort(self) -> QuerySet:
        return self.query.order_by(*self.fields)
