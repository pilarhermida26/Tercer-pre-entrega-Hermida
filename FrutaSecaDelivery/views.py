from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse
from FrutaSecaDelivery.models import Cuenta, Avatar
from FrutaSecaDelivery.forms import formSetCuenta, UserEditForm, ChangePasswordForm, AvatarForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.models import User


# Create your views here.
@login_required
def inicio(request):
    avatar = getavatar(request)
    return render (request, "FrutaSecaDelivery/inicio.html", {"avatar": avatar})

def productos(request):
    return render (request, "FrutaSecaDelivery/productos.html")

def pedidos(request):
    return render (request, "FrutaSecaDelivery/MisPedidos.html")

def cuentas(request):
    Cuentas = Cuentas.objects.all()
    return render(request, "FrutaSecaDelivery/cuentas.html",{"Cuentas":Cuentas})

def envios(request):
    return render (request, "FrutaSecaDelivery/envios.html")
@login_required
def setCuentas(request):
    Cuentas = Cuenta.objects.all()
    if request.method == 'POST':
        cuenta = Cuenta(nombre=request.POST["nombre"],apellido=request.POST["apellido"], email=request.POST["email"])
        cuenta.save()
        miFormulario = formSetCuenta(request.POST)
        return render(request,"FrutaSecaDelivery/setCuentas.html", {"miFormulario":miFormulario, "Cuentas":Cuentas})    
          
    else:
        miFormulario = formSetCuenta()
    return render(request, "FrutaSecaDelivery/setCuentas.html", {"miFormulario":miFormulario, "Cuentas":Cuentas})

    """if request.method == 'POST':
        cuenta = Cuenta(nombre=request.POST["nombre"],apellido=request.POST["apellido"], email=request.POST["email"])
        cuenta.save()
        return render(request,"FrutaSecaDelivery/inicio.html")
    return render(request, "FrutaSecaDelivery/setCuentas.html")"""


def getCuentas(request):
    return render(request, "FrutaSecaDelivery/getCuentasa.html")

def buscarCuenta(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        Cuentas = Cuenta.objects.filter(nombre = nombre)
        return render(request, "FrutaSecaDelivery/getCuentas.html", {"Cuenta":Cuentas})
    else:
        respuesta = "No se enviaron datos"
    
    return HttpResponse(respuesta)

def eliminarCuenta(request, nombre_cuenta):
    cuenta = Cuenta.objects.get(nombre= nombre_cuenta)
    cuenta.delete()
    miFormulario = formSetCuenta()
    Cuentas = Cuenta.objects.all()
    return render(request, "FrutaSecaDelivery/setCuentas.html", {"miFormulario":miFormulario, "Cuentas":Cuentas})

def editarCuenta(request, nombre_cuenta):
    cuenta = Cuenta.objects.get(nombre= nombre_cuenta)
    if request.method == 'POST':
        miFormulario = formSetCuenta(request.POST)
        if miFormulario.is_valid:
            print(miFormulario)
            data = miFormulario.cleaned_data

            cuenta.nombre = data['nombre']
            cuenta.apellido = data['apellido']
            cuenta.email = data['email']
            cuenta.save()
            miFormulario = formSetCuenta()
            Cuentas = Cuenta.objects.all()
            return render(request, "FrutaSecaDelivery/setCuentas.html", {"miFormulario":miFormulario, "Cuentas":Cuentas})
    else:
        miFormulario = formSetCuenta(initial={'nombre': cuenta.nombre, 'apellido': cuenta.apellido, 'email': cuenta.email})
    return render(request, "FrutaSecaDelivery/editarCuenta.html", {"miFormulario":miFormulario})


def loginWeb(request):
    if request.method == "POST":
        user = authenticate(username = request.POST['user'], password = request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect("../inicio")
        else:
            return render(request, 'FrutaSecaDelivery/login.html', {'error': 'Usuario o contraseña incorrectos'})
    else:
        return render(request, 'FrutaSecaDelivery/login.html')

def registro(request):
    if request.method == "POST":
        userCreate = UserCreationForm(request.POST)
        if userCreate is not None:
            userCreate.save()
            return render(request, 'FrutaSecaDelivery/login.html')
    else:
        return render(request, 'FrutaSecaDelivery/registro.html')

@login_required  
def perfilview(request):
    return render(request, 'FrutaSecaDelivery/Perfil/Perfil.html')

@login_required  
def editarPerfil(request):
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    if request.method == "POST":
        form = UserEditForm(request.POST, instance = usuario)
        if form.is_valid():
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            user_basic_info.save()
            return render(request, 'FrutaSecaDelivery/Perfil/Perfil.html')
    else:
        form = UserEditForm(initial= {'username': usuario.username, 'email': usuario.email, 'first_name': usuario.first_name, 'last_name': usuario.last_name })
        return render(request, 'FrutaSecaDelivery/Perfil/editarPerfil.html', {"form": form})

@login_required
def changePassword(request):
    usuario = request.user    
    if request.method == "POST":
        form = ChangePasswordForm(data = request.POST, user = usuario)
        if form.is_valid():
            if request.POST['new_password1'] == request.POST['new_password2']:
                user = form.save()
                update_session_auth_hash(request, user)
            return HttpResponse("Las constraseñas no coinciden")
        return render(request, "FrutaSecaDelivery/inicio.html")
    else:
        form = ChangePasswordForm(user = usuario)
        return render(request, 'FrutaSecaDelivery/Perfil/changePassword.html', {"form": form})

def editAvatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            user = User.objects.get(username = request.user)
            avatar = Avatar(user = user, image = form.cleaned_data['avatar'], id = request.user.id)
            avatar.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None           
            return render(request, "FrutaSecaDelivery/inicio.html", {'avatar': avatar})
    else:
        try:
            avatar = Avatar.objects.filter(user = request.user.id)
            form = AvatarForm()
        except:
            form = AvatarForm()
    return render(request, "FrutaSecaDelivery/Perfil/avatar.html", {'form': form})

def getavatar(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return avatar