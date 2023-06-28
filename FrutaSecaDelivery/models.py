from django.db import models

# Create your models here.

class Producto(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    #def #__str__(self):
        #return f"nombre: {self.nombre} - camada: {self.camada}"

class MiCuenta(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class MisPedidos(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

class Envios(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()





