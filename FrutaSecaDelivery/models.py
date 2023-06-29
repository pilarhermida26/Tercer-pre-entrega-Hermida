from django.db import models

# Create your models here.

class Producto(models.Model):

    nombre = models.CharField(max_length=40)
    tipo = models.IntegerField()


class MiCuenta(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class MisPedidos(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    

class Envios(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()





