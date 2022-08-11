from django.urls import path
from . import views

#Este nombre se coloca por si tenemos otras rutas iguales que no colisionen entre si, si no que añadiendo el namespace delante listo {% url 'carro:agregar' producto.id %}
app_name = "carro"

urlpatterns = [
    # path('', views.servicio, name="Carro"),
    path("agregar/<int:producto_id>/", views.agregar_producto, name="agregar"),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name="eliminar"),
    path('restar/<int:producto_id>/', views.restar_producto, name="restar"),
    path('limpiar/', views.limpiar_carro, name="limpiar"),
]
