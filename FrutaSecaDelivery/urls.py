from django.urls import path
from FrutaSecaDelivery.views import * 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inicio/', inicio),
    path('productos/', productos, name="Productos"),
    path('envios/', envios,name="Envios"),
    path('cuentas/', cuentas, name="Cuenta"),
    path('MisPedidos/', pedidos, name="MisPedidos"),
    path('setCuentas/', setCuentas, name="setCuenta"),
    path('getCuentas/', getCuentas, name="getCuenta"),
    path('buscarCuenta/', buscarCuenta, name="buscarCuenta"),
    path('eliminarCuenta/<nombre_cuenta>', eliminarCuenta, name="eliminarCuenta"),
    path('editarCuenta/<nombre_cuenta>', editarCuenta, name="editarCuenta"),
    path('editarCuenta/<nombre_cuenta>', editarCuenta, name="editarCuenta"),
    path('login/', loginWeb, name="login"),
    path('registro/', registro, name="registro"),
    path('Logout/',LogoutView.as_view(template_name = 'FrutaSecaDelivery/login.html'), name="Logout"),
    path('perfil/', perfilview, name="perfil"),
    path('Perfil/editarPerfil/', editarPerfil, name="editarPerfil"),
    path('Perfil/changePassword/', changePassword, name="changePassword"),
    path('Perfil/changeAvatar/', editAvatar, name="editAvatar"),
]