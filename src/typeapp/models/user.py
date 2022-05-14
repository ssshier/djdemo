from django.db import models
from core.models.base import BaseColumns


class User(BaseColumns):

    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
