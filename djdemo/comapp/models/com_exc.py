from django.db import models
from core.models.base import BaseColumns


class ComExc(BaseColumns):
    app_code: str = models.CharField(max_length=32)
    app_name: str = models.CharField(max_length=32)
    module_code: str = models.CharField(max_length=32)
    module_name: str = models.CharField(max_length=32)
    name: str = models.CharField(max_length=32)
    code: str = models.CharField(max_length=32)
    message: str = models.CharField(max_length=128)
