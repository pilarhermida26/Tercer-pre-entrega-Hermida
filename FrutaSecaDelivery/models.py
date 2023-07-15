from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Producto(models.Model):

    nombre = models.CharField(max_length=40)
    tipo = models.IntegerField()


class Cuenta(models.Model):
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

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatares', null = True, blank = True)





