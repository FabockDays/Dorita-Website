from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from mainapp.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# inicio


def index(request):
    
    return render(request, 'mainapp/index.html', {
        'title' : 'Inicio'
    })

# Mujer


def Mremeras(request):
    
    

    return render(request, 'mainapp/mujer/mujer-remeras.html',{
        'title' : 'Remeras'
    })



def Mjeans(request):
    return render(request, 'mainapp/mujer/mujer-jeans.html',{
        'title' : 'Jeans'
    })

def Mcamisetas(request):
    return render(request, 'mainapp/mujer/mujer-camisetas.html',{
        'title' : 'Camisetas'
    })

def Mcalzas(request):
    return render(request, 'mainapp/mujer/mujer-calzas.html', {
        'title' : 'Calzas'
    })

def Mjoggins(request):
    return render(request, 'mainapp/mujer/mujer-joggins.html', {
        'title' : 'Joggins'
    })

def Mpijamas(request):
    return render(request, 'mainapp/mujer/mujer-pijamas.html',{
        'title' : 'Pijamas'
    })

# Hombre


def Hremeras(request):
    return render(request, 'mainapp/hombre/hombre-remeras.html',{
        'title' : 'Remeras'
    })

def Hjeans(request):
    return render(request, 'mainapp/hombre/hombre-jeans.html',{
        'title' : 'Jeans'
    })

def Hjoggins(request):
    return render(request,  'mainapp/hombre/hombre-joggins.html',{
        'title' : 'Joggins'
    })

def Hcamisetas(request):
    return render(request, 'mainapp/hombre/hombre-camisetas.html',{
        'title' : 'Camisetas'
    })

# Accesorios

def Amochilas(request):
    return render(request, 'mainapp/accesorios/accesorios-mochilas.html',{
        'title' : 'Mochilas'
    })

def Abolsos(request):
    return render(request, 'mainapp/accesorios/accesorios-bolsos.html',{
        'title' : 'Bolsos'
    })
def Ariñoneras(request):
    return render(request, 'mainapp/accesorios/accesorios-riñoneras.html',{
        'title' : 'Riñoneras'
    })

def Abandoleras(request):
    return render(request, 'mainapp/accesorios/accesorios-bandoleras.html',{
        'title' : 'Bandoleras'
    })


# Ofertas
@login_required(login_url="login")
def Ofertas(request):
    return render(request, 'mainapp/ofertas.html',{
        'title' : "Ofertas"
    })

# Registro y login

def Registro_usuarios(request):

    formulario_registro = RegisterForm()

    if request.method == 'POST':
        formulario_registro = RegisterForm(request.POST)
    
    if formulario_registro.is_valid():
        formulario_registro.save()

        messages.success(request, 'Te has registrado correctamente')

        

        return redirect('ofertas')



    return render(request, 'mainapp/usuarios/registro.html',{
        'title' : 'Registro',
        'formulario_registro' : formulario_registro
    })

def Login_Page(request):
    
    if request.method ==  'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None :
            login(request, user)

            return redirect('inicio')

        else:
            messages.warning(request, 'No te has identificado correctamente')

    return render(request, 'mainapp/usuarios/login.html',{
        'title' : 'Identificate'
    })

@login_required(login_url="login")
def Logout_user(request):
    logout(request)
    return redirect('login')