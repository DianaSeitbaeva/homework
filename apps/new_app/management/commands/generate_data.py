from typing import Any
from datetime import datetime

from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth.models import(
    User,
)
from new_app.models import(
    Group,
    Account,
    Student,
    Professor,
)


class Command(BaseCommand):
    """Custom command for filling up database.

    Test data only
    """

    help = 'Custom command for filling up database.'

    def __init__(self, *args: tuple, **kwargs: dict) -> None:
        pass

    def _generate_students(self) -> None:
        STUDENT_COUNT = 100

        def _generate_account(i: int) -> str:
            return f'Пользователь{i}'
        
        def _generate_student(i:int) -> str:
            return f'Студент{i}'

        i: int
        for i in range(STUDENT_COUNT):
            account_user: str = _generate_account(i)
            account_student: str = _generate_student(i)
            rand_int = random.randint(0,20)
            Student.objects.create(
                age = random.randint(16,27),
                gpi = random.randint(2,12),
                group = 
                account=Account.objects.create(
                    user=User.objects.create(
                        username=account_user
                    )
                )
            )

    def _generate_groups(self) -> None:
        """Generate Group objs."""
        def generate_name(inc:int) -> str:
            return f'Группа {inc}'

        inc: int
        for inc in range(20):
            name: str = generate_name(inc)
            Group.objects.create(
                name=name
            )

    def handle(self, *args: tuple, **kwargs: dict) -> None:
        """Handles data filling."""

        start: datetime = datetime.now()

        self._generate_groups()
        print(
            'Generating Data: {} seconds'.format(
            (datetime.now()-start).total_seconds()
            )
        )