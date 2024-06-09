from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Login_Professor, name='Login_Professor'),
    path('Cadastro/', views.Cadastro, name='Cadastro'),
    path('CadastrarTurma/<int:id>/', views.Cadastro_Turma, name='Cadastro_Turma'),
    path('CadastrarAtividade/<int:id>/', views.Cadastro_Atividades, name='Cadastrar_Atividade'),
]
