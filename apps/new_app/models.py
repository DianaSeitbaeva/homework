from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    ACCOUNT_FULL_NAME_MAX_LENGTH = 20
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    full_name = models.CharField(
        max_length=ACCOUNT_FULL_NAME_MAX_LENGTH
    )
    description = models.TextField()

    def __str__(self) -> str:
        return f'Account: {self.user.id} / {self.full_name}'
    
    class Meta:
        ordering = (
            'full_name',
            )
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'

class Group(models.Model):
    GROUP_NAME_MAX_LENGTH = 10
    name = models.CharField(
        max_length=GROUP_NAME_MAX_LENGTH
    )
    def __str__(self) -> str:
        return f'Group: {self.name}' 

    
    class Meta:
        ordering = (
            'name',
        )
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'



class Student(models.Model):
    #один аккаунт = много студентов

    account=models.OneToOneField(
        Account, 
        on_delete=models.CASCADE)

    age=models.IntegerField(
        'Возраст студента')

    group=models.ForeignKey(
        Group, on_delete=models.PROTECT
    )
    GPA=models.FloatField(
        'Средний значение GPA'
    )

    def __str__(self) -> str:
        return f'Student: {self.account}, Age: {self.age}, group: {self.group}, GPA: {self.GPA}' 

    
    class Meta:
        ordering = (
            'account',
            'age',
            'group',
            'GPA',
        )
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
