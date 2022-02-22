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

def index_3(request: WSGIRequest) -> HttpResponse:
    users: QuerySet = User.objects.all()
    context: dict = {
        'ctx_title': 'Главная страница',
        'ctx_users' : users,
    }
    return render(
        request,
        'index.html',
        context,
    )

def admin(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        'admin.html',
        context = {"ctx_users":User.objects.all()}
    )

def show(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        'show.html',
        context,
    )