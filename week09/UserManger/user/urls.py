from django.urls import path, re_path, register_converter
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login_user),
    path('index', views.index, name='index')
]
