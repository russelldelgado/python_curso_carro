from django.urls import path
from .views import VRegistro, cerrar_sesion,logear

#Este nombre se coloca por si tenemos otras rutas iguales que no colisionen entre si, si no que añadiendo el namespace delante listo {% url 'carro:agregar' producto.id %}

urlpatterns = [
    # path("", views.login, name="Login"),
    path('', VRegistro.as_view(), name="Autenticacion"),
    path('Login', logear, name="Login"),
    path('cerrar_sesion', cerrar_sesion, name="Cerrar_sesion"),
]
