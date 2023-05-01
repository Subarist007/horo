from django.db import models
from django.contrib.auth.models import AbstractUser


"""Расширение класса добавлением даты рождения"""
class User(AbstractUser):
    date_birth = models.DateField(null=True)

