from django.http import HttpResponse
from django.template import Template, Context, loader

def saludo(request):
    return HttpResponse("hola django equipo coder")

def segunda_vista(request):
    return HttpResponse("<br><br> <h1>Hola mundo!</h1>")

def miNombreEs(self, nombre):
    data = f"Mi nombre es: <h1>{nombre}</h1>"

    return HttpResponse(data)

def probandoTemplate(self):
    nombre = "Pilar"
    apellido = "Hermida"
    namelist = ["Gabriel", "Ignacio", "Patricia", "Juan"]
    

    diccionario = {"nombre": nombre, "apellido": apellido, "namelist": namelist}
   

    
    plantilla = loader.get_template("template1.html")

    
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)






    