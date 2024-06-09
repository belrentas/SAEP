from django.shortcuts import render, get_object_or_404, redirect                    # REQUESTS PADROES DJANGO
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout                         # REQUERIMENTO DE LOGIN
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
            return render(request, 'core/area_professor.html')
        
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
            return redirect(f'/area_professor/{request.user.id}')
        else:
            return HttpResponse('Verifique os campos')

#area da turma
def area_turma(request, id):
    if request.method == 'GET':
        turma = get_object_or_404(Turma, pk=id)
        atividades = Atividades.objects.all()

        context = {
            'turma': turma,
            'atividades': atividades,
        }
        return render(request, 'core/area_turma.html', context)

#cadastro Atividades
def Cadastro_Atividades(request, id_usuario, id_turma):
    usuario = get_object_or_404(User, pk=id_usuario)
    turma = get_object_or_404(Turma, pk=id_turma)

    context = {
        'usuario': usuario,
        'turma': turma
    }

    if request.method == 'GET':
        return render(request, 'core/cadastro_atividades.html', context)
    else:
        nome_atividade = request.POST.get('Nome_Atividade')

        atividade = Atividades.objects.create(
            Nome_item = nome_atividade,
            id_usuario = usuario,
            First_Name = usuario.first_name,
            id_lista = turma,
            Nome_Turma = turma.Nome_Turma,
        )
        atividade.save()
        return redirect(f'/area_turma/{request.user.id}')

#area do professor
def area_professor(request, id):
    if request.method == 'GET':
        turmas = Turma.objects.all()
        return render(request, 'core/area_professor.html', {'turmas': turmas})
    
