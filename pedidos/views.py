from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from carro.carro import Carro
from pedidos.models import LineasPedido, Pedido
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
# Create your views here.


def pedidos(request):
    return render(request , "pedidos/pedido.html")


@login_required(login_url="/autenticacion/Login")
def  procesar_pedido(request):
    pedido = Pedido.objects.create(user = request.user)
    print(request.user)
    # print(pedido)
    carro = Carro(request)
    lineas_pedido = list()
    for key, value in carro.carro.items():
        print('--------------------------------------')
        print(f'usuario : {request.user.username} , email : {request.user.email} , usuario general : {request.user}')
        print('--------------------------------------')
        lineas_pedido.append(
            LineasPedido(
                producto_id = key,
                cantidad = value['cantidad'],
                user = request.user,
                pedido_id = pedido.id,
            )
        )
    
    carro.limpiar_carro()

    enviar_email(
        pedido = pedido,
        lineas_pedido = lineas_pedido,
        nombre_usuario = request.user.username,
        email_usuario = request.user.email
    )
    
    LineasPedido.objects.bulk_create(lineas_pedido)

    messages.success(request , "Pedido creado correctamente")
    return redirect('Home')

def enviar_email(**kwargs):
    asunto = "Gracias por el pedido"

    mensaje = render_to_string("emails/pedido.html",{
        "pedido" : kwargs.get('pedido'),
        "lineas_pedido" : kwargs.get('lineas_pedido') ,
        "nombre_usuario": kwargs.get('nombre_usuario'),
        "email_usuario": kwargs.get('email_usuario')
    })
    #eliminar todo lo que tenga que ver con etiquetas html
    mensaje_texto = strip_tags(mensaje)
    from_email = "russellwallstreet@gmail.com"
    # to = kwargs.get('emailusuario')
    to = "rjdelgado@deditec.es"
    print(f'asunto : {asunto}, mensaje de texto : {mensaje_texto}, from_mail : {from_email}, to : {to} , html message : {mensaje}')
    send_mail(
        asunto,
        mensaje_texto,
        from_email,
        [to],
        html_message=mensaje,
    )
    


