from .manager import UserManager
from common.models import IndexedTimeStampedModel
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


class User(AbstractBaseUser, PermissionsMixin, IndexedTimeStampedModel):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    karma = models.IntegerField(default=0)
    avatar = models.ImageField(blank=True, default='avatar.jpg')
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username
    
