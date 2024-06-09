from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Login_Professor, name='Login_Professor'),
    path('Cadastro/', views.Cadastro, name='Cadastro'),
]
