from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render

from new_app.models import (
    Account, 
    Student
)

def index(request: WSGIRequest) -> HttpResponse:

    
    user: User = User.objects.first()
    username: str = user.username
    acc: Account = Account.objects.get(user_id=user.id)
    name: str = acc.full_name
    student: Student = Student.objects.get(account_id=user.id)
    gpa: int = student.GPA

    text: str = f'Username: {username}, Name: {name}, GPA: {gpa}'

    response: HttpResponse = HttpResponse(text)
    return response

def index_2(request: WSGIRequest) -> HttpResponse:
    return HttpResponse(
        '<h1>Страница: Стартовая</h1>'
    )