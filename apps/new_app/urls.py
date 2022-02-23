from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [


    path('', views.index_3),
    path('index_2/', views.index_2),
    path('index_3/', views.index_3),
    path('admin/', views.admin),
    path('show/', views.show),
    
]