from django.db import models
from core.models.base import BaseColumns


class User(BaseColumns):
    username: str = models.CharField(max_length=50, unique=True)
    password: str = models.CharField(max_length=50)
    email: str = models.EmailField(max_length=50, unique=True)
    is_active: bool = models.BooleanField(default=True)
