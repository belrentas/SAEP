from django.shortcuts import render, get_object_or_404, redirect                    # REQUESTS PADROES DJANGO
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout                         # REQUERIMENTO DE LOGIN
from django.contrib.auth.decorators import login_required
from core.models import *


# Create your views here.
def Login_Professor(request):
    if request.method == 'GET':
        return render(request, 'core/login.html')
    else:
        Email_Professor = request.POST.get('Email_Professor')
        Senha_Professor = request.POST.get('Senha_Professor')

        usuario = authenticate(username=Email_Professor, password=Senha_Professor)

        if usuario:
            login(request, usuario)
            # return redirect('area_professor.html')
            return HttpResponse('foda')
        
        else:
            return HttpResponse('E-mail ou Senha incorretos')
        
#Cadastrar Professor
def Cadastro(request):
    if request.method == 'GET':
        return render(request, 'core/cadastro.html')
    else:
        Nome_Professor = request.POST.get('Nome_Professor')
        Sobrenome_Professor = request.POST.get('Sobrenome_Professor')
        Senha_Professor = request.POST.get('Senha_Professor')
        Email_Professor = request.POST.get('Email_Professor')

        if Nome_Professor and Sobrenome_Professor and Senha_Professor and Email_Professor !='':
            usuario = User.objects.filter(username=Email_Professor).first()
            if usuario:
                return HttpResponse('Esse E-mail ja existe!')
            else:
                usuario = User.objects.create_user(

                    first_name=Nome_Professor,
                    last_name=Sobrenome_Professor,
                    email=Email_Professor,
                    username=Email_Professor, 
                )

                usuario.set_password(Senha_Professor)
                usuario.save()
                return redirect('/')
            
#Cadastro Turma 
def Cadastro_Turma(request, id):
    usuario = get_object_or_404(User, pk=id)
    if request.method == 'GET':
        return render(request, 'core/cadastro_turma.html')
    else:
        nome_Turma = request.POST.get('Nome_Turma')

        if nome_Turma != '':
            turma = Turma.objects.create(
                Nome_Turma = nome_Turma,
                id_usuario = usuario,
                First_Name = usuario.first_name,
            )
            turma.save()
            return HttpResponse('Turma cadastrada')
        else:
            return HttpResponse('Verifique os campos')

#cadastro Atividades
def Cadastro_Atividades(request, id):
    usuario = get_object_or_404(User, pk=id)
    turmas = Turma.objects.all()
    if request.method == 'GET':
        return render(request, 'core/cadastro_atividades.html',{'turmas': turmas})
    else:
        nome_atividade = request.POST.get('Nome_Atividade')
        nome_turma = request.POST.get('Turmas')
        for turma in turmas:
            if turma.Nome_Turma in nome_turma:
                if nome_atividade != '':
                    atividade = Atividades.objects.create(
                        Nome_item = nome_atividade,
                        id_usuario = usuario,
                        First_Name = usuario.first_name,
                        id_lista = turma, 
                        Nome_Turma = nome_turma,
                    )
                    atividade.save()
                    return HttpResponse('Atividade cadastrada')
                else:
                    return HttpResponse('Verifique os campos')