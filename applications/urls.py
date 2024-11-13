from django.urls import path
from django.contrib import admin
from .import views

urlpatterns = [
    path('application' ,  views.application , name = 'application') ,
    path('admin/', admin.site.urls),
]