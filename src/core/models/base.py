from typing import Any
from django.db import models


class BaseManager(models.Manager):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(BaseManager, self).__init__(*args, **kwargs)
        self.alive_only: bool = kwargs.get('alive_only', True)

    def get_queryset(self):
        if self.alive_only:
            return BaseQuerySet(self.model).filter(is_deleted=False)


class BaseQuerySet(models.QuerySet):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(BaseQuerySet, self).__init__(*args, **kwargs)


class BaseColumns(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=50, default="system")
    updated_by = models.CharField(max_length=50, default="system")
    is_deleted = models.BooleanField(default=False)

    objects = BaseManager()

    class Meta:
        abstract = True
