from tkinter import OUTSIDE
from django.shortcuts import render,redirect
from .carro import Carro
from tienda.models import Producto

# Create your views here.


def servicio(request):
    return render(request,"carro/carro.html")



def agregar_producto (request , producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.agregar(producto)
    return redirect('Tienda')




def eliminar_producto (request , producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.eliminar(producto)
    return redirect('Tienda')


def restar_producto (request , producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.restar_producto(producto)
    return redirect('Tienda')

def limpiar_carro (request):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect('Tienda')