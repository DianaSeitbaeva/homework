from datetime import datetime
from distutils.command import upload
import email
from enum import unique
from django.contrib.auth.models import (
    AbstractBaseUser, 
    PermissionsMixin,
)
from django.db import (
    models, 
)

from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.forms import (
    BooleanField, 
    CharField, 
    FileField, 
    ImageField,
)

from django.utils import timezone


from apps.abstracts.models import AbstractDateTime


class CustomUserManager(BaseUserManager):

    def create_user(
        self,
        email: str,
        password: str,
        **kwargs: dict
    ) -> 'CustomUser':
        if not email:
            raise ValidationError('Email required')

        user: 'CustomUser' = self.model(
            email = self.normalize_email(email),
            password=password
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        email: str,
        password: str,
        **kwargs: dict
    ) -> 'CustomUser':
        user: 'CustomUser' = self.model(
            email = self.normalize_email(email),
            password=password
        )
        user.is_staff=True
        user.is_superuser=True
        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        'Почта/Логин', unique=True
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        ordering = (
            'date_joined',
        )
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class File(AbstractDateTime):
    title_file = models.CharField(
        max_length=35,
    )
    file = models.FileField(
        upload_to='%d.%m.%Y',
        max_length=150,
    )
    

class Homework(AbstractDateTime):
    title_homework = models.CharField(
        max_length=35,
    ) 
    subject = models.CharField(
        max_length=35,
    ) 
    logo = models.ImageField(
        upload_to='%d.%m.%Y',
    )
    is_checked = models.BooleanField(
        max_length=35
    )
    homework = models.ForeignKey(
        File, 
        on_delete=models.PROTECT,
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
    )

class FileQuerySet(models.QuerySet):
    def get_is_checked(self) -> models.QuerySet:
        return self.filter(
            homework__is_checked = True
        )
