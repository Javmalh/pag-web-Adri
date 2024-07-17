from django.http import HttpResponse, JsonResponse
from .models import Contacto
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

def index(request):
    return render(request, 'index.html')

def producto_1(request):
    return render(request, 'producto_1.html')

def producto_2(request):
    context={}
    return render(request, 'producto_2.html',context) 

def producto_3(request):
    context={}
    return render(request, 'producto_3.html',context)

def producto_4(request):
    context={}
    return render(request, 'producto_4.html',context)

def contacto(request):
    return render(request, 'contacto.html')

def carrito(request):
    return render(request, 'carrito.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('index')
            
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "El usuario ya existe."})
            
        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Contraseñas no coinciden."})
    
def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm()
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm(),
                'error': 'El usuario o Contraseña no es válido/a'
            })
        else:
            login(request, user)    
            return redirect('index')    