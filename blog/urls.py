"""Created on 20200307_ABD"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.port_list, name='port_list')
]