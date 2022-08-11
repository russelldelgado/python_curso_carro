from django.shortcuts import render
from servicios.models import Servicio

# Create your views here.



def servicio(request):

    #primero tenemos que cargar todos nuestros servicios
    servicios = Servicio.objects.all()

    #posteriormente decirle a la vista que muestr todos nuestro servicios 

    return render(request,"servicios/servicio.html", {'servicios': servicios})