from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from abstracts.models import AbstractDateTime
from django.db.models import QuerySet

class AccountQuerySet(QuerySet):

    def get_superusers(self) -> QuerySet:
        return self.filter(
            user__is_superuser=True
        )


class Account(AbstractDateTime):
    ACCOUNT_FULL_NAME_MAX_LENGTH = 20
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    full_name = models.CharField(
        max_length=ACCOUNT_FULL_NAME_MAX_LENGTH
    )
    description = models.TextField()

    objects = AccountQuerySet().as_manager()

    def __str__(self) -> str:
        return f'Account: {self.user.id} / {self.full_name}'
    
    class Meta:
        ordering = (
            'full_name',
            )
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'

# class GroupQuerySet(QuerySet):
#     HIGH_GPA_LEVEL = 4.0

#     def get_students_with_high_gpa(self) -> QuerySet:
#         return self.filter(
#             self.Student_set().GPA__gte=self.HIGH_GPA_LEVEL
#         )

class Group(AbstractDateTime):
    GROUP_NAME_MAX_LENGTH = 10
    name = models.CharField(
        max_length=GROUP_NAME_MAX_LENGTH
    )
    #objects = GroupQuerySet().as_manager()

    def __str__(self) -> str:
        return f'Group: {self.name}' 

    
    class Meta:
        ordering = (
            'name',
        )
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class StudentQuerySet(QuerySet):
    ADULT_AGE = 18
    HIGH_GPA_LEVEL = 4.0

    def get_adult_students(self) -> QuerySet:
        return self.filter(
            age__gte=self.ADULT_AGE
        )


class Student(AbstractDateTime):
    MAX_AGE = 27
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
    objects = StudentQuerySet().as_manager()

    def __str__(self) -> str:
        return f'Student: {self.account}, Age: {self.age}, group: {self.group}, GPA: {self.GPA}' 


    def save(
        self,
        *args: tuple,
        **kwargs: dict
    ) -> None:
        if self.age > self.MAX_AGE:
            raise ValidationError(
                f'Допустимый возраст: {self.MAX_AGE}'
            )
            #self.age = self.MAX_AGE
        super().save(*args, **kwargs)

    def delete(self) -> None:
        breakpoint()
        datetime_now: datetime = datetime.now()

        self.datetime_deleted = datetime_now

        self.save(
            update_fields = ['datetime_deleted']
        )

    
    class Meta:
        ordering = (
            'account',
            'age',
            'group',
            'GPA',
        )
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Professor(AbstractDateTime):
    FULL_NAME_MAX_LENGTH = 20

    TOPIC_JAVA = 'java'
    TOPIC_PYTHON = 'python'
    TOPIC_TS = 'typescript'
    TOPIC_JS = 'javascript'
    TOPIC_RUBY = 'ruby'
    TOPIC_GO = 'golang'
    TOPIC_SQL = 'sql'
    TOPIC_SWIFT = 'swift'
    TOPIC_PHP = 'php'
    TOPIC_DELPHI = 'delphi'
    TOPIC_PERL = 'perl'

    TOPIC_CHOICES = (
        (TOPIC_JAVA,'Java'),
        (TOPIC_PYTHON,'Python'),
        (TOPIC_TS,'TypeScript'),
        (TOPIC_JS,'JavaScript'),
        (TOPIC_RUBY,'Ruby'),
        (TOPIC_GO,'Golang'),
        (TOPIC_SQL,'SQL'),
        (TOPIC_SWIFT,'Swift'),
        (TOPIC_PHP,'PHP'),
        (TOPIC_DELPHI,'Delphi'),
        (TOPIC_PERL,'Perl'),
    )

    full_name = models.CharField(
        verbose_name='полное имя', 
        max_length=FULL_NAME_MAX_LENGTH)
    topic = models.CharField(
        verbose_name='предмет',
        choices=TOPIC_CHOICES,
        default=TOPIC_PYTHON,
        max_length=FULL_NAME_MAX_LENGTH
    )
    students = models.ManyToManyField(
        Student
    )

    def __str__(self) -> str:
        return f'Professor: {self.full_name}, Topic: {self.topic}' 

    def save(
        self,
        *args: tuple,
        **kwargs: dict
    ) -> None:
        if self.full_name.__len__() > self.FULL_NAME_MAX_LENGTH:
            raise ValidationError(
                f'Допустимая длинна имени: {self.FULL_NAME_MAX_LENGTH}'
            )
            #self.age = self.MAX_AGE
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = (
            'full_name',
            'topic',
        )
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'