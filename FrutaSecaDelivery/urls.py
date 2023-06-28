from django.urls import path
from FrutaSecaDelivery.views import * #inicio,productos,envios,MiCuenta,MisPedidos,setMiCuenta, getMiCuenta, buscarMiCuenta

urlpatterns = [
    path('inicio/', inicio),
    path('productos/', productos, name="Productos"),
    path('envios/', envios,name="Envios"),
    path('MiCuenta/', MiCuenta, name="MiCuenta"),
    path('MisPedidos/', MisPedidos, name="MisPedidos"),
    path('setMiCuenta/', setMiCuenta, name="setMiCuenta"),
    path('getMiCuenta/', getMiCuenta, name="getMiCuenta"),
    path('buscarMiCuenta/', buscarMiCuenta, name="buscarMiCuenta"),
]