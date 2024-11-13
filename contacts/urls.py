from django.urls import path
from django.contrib import admin
from .import views

urlpatterns = [
    path('contact' ,  views.contact , name = 'contact') ,
]