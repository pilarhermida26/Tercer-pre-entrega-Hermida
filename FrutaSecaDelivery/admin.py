from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Producto)
admin.site.register(MiCuenta)
admin.site.register(MisPedidos)
admin.site.register(Envios)