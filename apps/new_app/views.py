from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from auths.models import CustomUser
from django.shortcuts import render

from new_app.models import (
    # Account, 
    Student
)

def index(request: WSGIRequest) -> HttpResponse:

    
    user: CustomUser = CustomUser.objects.first()
    username: str = user.username
    acc: CustomUser = CustomUser.objects.get(user_id=user.id)
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

def admin(request: WSGIRequest) -> HttpResponse:
    users: QuerySet = CustomUser.objects.all()
    context: dict = {
        'ctx_title': 'Главная страница',
        'ctx_users' : users,
    }
    return render(
        request,
        'admin.html',
        context,
    )

def show(request: WSGIRequest, username: str) -> HttpResponse:
    users: QuerySet = CustomUser.objects.get(
        username=username
    )
    context: dict = {
        'ctx_title': 'Профиль пользователя',
        'ctx_users' : users,
    }
    return render(
        request,
        template_name='show.html',
        context=context,
    )