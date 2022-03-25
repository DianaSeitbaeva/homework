from http.client import HTTPResponse
from multiprocessing import context
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, QueryDict
from django.shortcuts import render
from django.template import loader
from django.contrib.auth import (
    authenticate as dj_authenticate,
    login as dj_login,
    logout as dj_logout,
)
from django.db.models import QuerySet
from django.views import View

from auths.forms import CustomUserChangeForm


# class StudentViewSet(ViewSet):
#     queryset
#     permission_classes
#     filters

class HttpResponsMixin(View):
    def get_return(templete_name, context):
        return HttpResponse(
            templete_name.render(
                context, request
            ),
            content_type='text/html'
        )
    

class IndexView(View):
    queryset: QuerySet = Homework.objects.get_not_deleted()

    def get(
        self,
        request,
        WSGIRequest,
        *args: tuple,
        **kwards: dict
    ):
        if not request.user.is_authenticated:
            return render(
                request,
                'login.html'
            )
        homeworks: QuerySet = self.queryset.filter(
            user=request.user
        )

        context: dict = {
        'ctx_title': 'Главная страница',
        'ctx_users' : homeworks,
        }

        template_name = loader.get_template(
            'index.html'
        )


from new_app.models import (
    # Account, 
    Student
)

from auths.models import (
    CustomUser,
    File,
    Homework,
)



# def index(request: WSGIRequest) -> HttpResponse:
#     if not request.user.is_authenticated:
#         return render(
#             request,
#             'login.html'
#         )
#     homework: QuerySet = Homework.objects.filter(
#         user=request.user
#     )
#     context: dict = {
#         'ctx_title': 'Главная страница',
#         'ctx_users' : homework,
#     }
#     return render(
#         request,
#         template_name='index.html',
#         context=context,
#     )

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

class LoginView(View):

    def post(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict
    ):
        if request.method == 'POST':
            email: str = request.POST['email']
            password: str = request.POST['password']

            user: CustomUser = dj_authenticate(
                email=email,
                password=password
            )
            
            
            if not user:
                return render(
                    request,
                    'login.html',
                    {'error_message': 'Невереные данные'}
                )
            if not user.is_active:
                return render(
                    request,
                    'login.html',
                    {'error_message': 'Ваш аккаунт был удален'}
                )
            dj_login(request, user)

            homeworks: QuerySet = Homework.objects.filter(
                user=request.user
            )
            return render(
                request,
                'index.html',
                {'homeworks': homeworks}
            )
        return render(
            request,
            'login.html'
        )

# def login(request: WSGIRequest) -> HttpResponse:

#     if request.method == 'POST':
#         email: str = request.POST['email']
#         password: str = request.POST['password']

#         user: CustomUser = dj_authenticate(
#             email=email,
#             password=password
#         )
#         # Guard Clause
#         #
#         if not user:
#             return render(
#                 request,
#                 'login.html',
#                 {'error_message': 'Невереные данные'}
#             )
#         if not user.is_active:
#             return render(
#                 request,
#                 'login.html',
#                 {'error_message': 'Ваш аккаунт был удален'}
#             )
#         dj_login(request, user)

#         homeworks: QuerySet = Homework.objects.filter(
#             user=request.user
#         )
#         return render(
#             request,
#             'index.html',
#             {'homeworks': homeworks}
#         )
#     return render(
#         request,
#         'login.html'
#     )

class LogoutView(View):
    def post(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict
    ):
        dj_logout(request)

        form: CustomUserChangeForm = CustomUserChangeForm(
            request.POST
        )
        context: dict = {
            'form': form,
        }
        return render(
            request,
            'login.html',
            context
        )


# def logout(request: WSGIRequest) -> HttpResponse:

#     dj_logout(request)

#     form: CustomUserChangeForm = CustomUserChangeForm(
#         request.POST
#     )
#     context: dict = {
#         'form': form,
#     }
#     return render(
#         request,
#         'login.html',
#         context
#     )


class RegisterView(View):
    
    def post(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs:  dict
    ):

        form: CustomUserChangeForm = CustomUserChangeForm(
        request.POST
        )
        if form.is_valid():
            user: CustomUser = form.save(
                commit=False
            )
            email: str = form.cleaned_data['email']
            password: str = form.cleaned_data['password']
            user.email = email
            user.set_password(password)
            user.save()

            user: CustomUser = dj_authenticate(
                email=email,
                password=password
            )
            if user and user.is_active:

                dj_login(request, user)

                homeworks: QuerySet = Homework.objects.filter(
                    user=request.user
                )
                return render(
                    request,
                    'index.html',
                    {'homeworks': homeworks}
                )
        context: dict = {
            'form': form
        }
        return render(
            request,
            'register.html',
            context
        )


# def register(request: WSGIRequest) -> HttpResponse:

#     form: CustomUserChangeForm = CustomUserChangeForm(
#         request.POST
#     )
#     if form.is_valid():
#         user: CustomUser = form.save(
#             commit=False
#         )
#         email: str = form.cleaned_data['email']
#         password: str = form.cleaned_data['password']
#         user.email = email
#         user.set_password(password)
#         user.save()

#         user: CustomUser = dj_authenticate(
#             email=email,
#             password=password
#         )
#         if user and user.is_active:

#             dj_login(request, user)

#             homeworks: QuerySet = Homework.objects.filter(
#                 user=request.user
#             )
#             return render(
#                 request,
#                 'index.html',
#                 {'homeworks': homeworks}
#             )
#     context: dict = {
#         'form': form
#     }
#     return render(
#         request,
#         'register.html',
#         context
#     )