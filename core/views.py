from django.shortcuts import render, get_object_or_404, redirect                    # REQUESTS PADROES DJANGO
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout                         # REQUERIMENTO DE LOGIN
from django.contrib.auth.decorators import login_required
from .models import * 


# Create your views here.
def Login_Professor(request):
    if request.method == 'GET':
        return render(request, 'core/login.html')
    else:
        Email_Usuario = request.POST.get('Email_Usuario')
        Senha_Usuario = request.POST.get('Senha_Usuario')

        usuario = authenticate(username=Email_Usuario, password=Senha_Usuario)

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
            
            