from django.urls import path
from FrutaSecaDelivery.views import * 

urlpatterns = [
    path('inicio/', inicio),
    path('productos/', productos, name="Productos"),
    path('envios/', envios,name="Envios"),
    path('MiCuenta/', cuenta, name="MiCuenta"),
    path('MisPedidos/', pedidos, name="MisPedidos"),
    path('setMiCuenta/', setCuenta, name="setMiCuenta"),
    path('getMiCuenta/', getCuenta, name="getMiCuenta"),
    path('buscarMiCuenta/', buscarCuenta, name="buscarMiCuenta"),
]