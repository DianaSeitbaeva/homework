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
    re_path(
        r'^show/(?P<username>\w+)/$',
        views.show,
        name='page_show'
    ),
    path('show/', views.show, name='page_show'),
    path('about/', views.show, name='page_about'),
    path('delete/', views.show, name='page_delete'),
]