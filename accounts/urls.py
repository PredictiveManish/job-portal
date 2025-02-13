from django.urls import path
from django.contrib import admin
from .import views

urlpatterns=[
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('admin/', admin.site.urls),
]