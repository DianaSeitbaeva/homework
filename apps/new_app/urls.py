from django.urls import (
    path,
    re_path,
)
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [

    path('', views.index),
    path('admin/', views.admin, name='page_main'),
    path(
        'show/<int:user_id>/',
        views.show,
        name='page_show'
    ),
    path('about/', views.show, name='page_about'),
    path('delete/', views.show, name='page_delete'),
    path('register/', views.register, name='page_register'),
    path('login/',    views.login,    name='page_login'),
    path('logout/',   views.logout,   name='page_logout'),
]