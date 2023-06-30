from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from FrutaSecaDelivery.models import MiCuenta
from FrutaSecaDelivery.forms import formSetMiCuenta


# Create your views here.

def inicio(request):
    return render (request, "FrutaSecaDelivery/inicio.html")

def productos(request):
    return render (request, "FrutaSecaDelivery/productos.html")

def pedidos(request):
    return render (request, "FrutaSecaDelivery/MisPedidos.html")

def cuenta(request):
    return render(request, "FrutaSecaDelivery/MiCuenta.html")

def envios(request):
    return render (request, "FrutaSecaDelivery/envios.html")

def setCuenta(request):
    if request.method == 'POST':
        miFormulario = formSetMiCuenta(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            data = miFormulario.cleaned_data
            MiCuenta = cuenta(nombre=data["nombre"],apellido=data["apellido"], email=data["email"])    
            MiCuenta.save()
            return render(request,"FrutaSecaDelivery/inicio.html")    
    else:
        miFormulario = formSetMiCuenta()
    return render(request, "FrutaSecaDelivery/setMiCuenta.html", {"miFormulario":miFormulario})

   

def getCuenta(request):
    return render(request, "FrutaSecaDelivery/getMiCuenta.html")

def buscarCuenta(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        MiCuenta = cuenta.objects.filter(nombre = nombre)
        return render(request, "FrutaSecaDelivery/getMiCuenta.html", {"MiCuenta":MiCuenta})
    else:
        respuesta = "No se enviaron datos"
    
    return HttpResponse(respuesta)