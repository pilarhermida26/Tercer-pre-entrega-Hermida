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

def MisPedidos(request):
    return render (request, "FrutaSecaDelivery/MisPedidos.html")

def MiCuenta(request):
    return render(request, "FrutaSecaDelivery/MiCuenta.html")

def envios(request):
    return render (request, "FrutaSecaDelivery/envios.html")

def setMiCuenta(request):
    if request.method == 'POST':
        miFormulario = formSetMiCuenta(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            data = miFormulario.cleaned_data
            MiCuenta = MiCuenta(nombre=data["nombre"],apellido=data["apellido"], email=data["email"])    
            MiCuenta.save()
            return render(request,"FrutaSecaDelivery/inicio.html")    
    else:
        miFormulario = formSetMiCuenta()
    return render(request, "FrutaSecaDelivery/setMiCuenta.html", {"miFormulario":miFormulario})

   

def getMiCuenta(request):
    return render(request, "FrutaSecaDelivery/getMiCuenta.html")

def buscarMiCuenta(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        MiCuenta = MiCuenta.objects.filter(nombre = nombre)
        return render(request, "FrutaSecaDelivery/getMiCuenta.html", {"MiCuenta":MiCuenta})
    else:
        respuesta = "No se enviaron datos"
    
    return HttpResponse(respuesta)