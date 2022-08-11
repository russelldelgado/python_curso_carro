from ast import If
from django.shortcuts import render, redirect
# Create your views here.
from .forms import FormularioContacto
from django.core.mail import EmailMessage


def contacto(request):

    formulario_contacto = FormularioContacto()

    if request.method == "POST" : 
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid() :
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
            
            
            email = EmailMessage(
                subject= "Mensaje desde app django"
            "El usuario con nombre {} y correo {} escribe lo siguiente \n\n : {}".format(nombre,email,contenido),
            reply_to=[email], from_email=["ganvapp.mailer.server@gmail.com"], to=[email], )

            email = EmailMessage(
            'Mensaje desde app django',
            "El usuario con nombre {} y correo {} escribe lo siguiente \n\n : {}".format(nombre,email,contenido),
            'ganvapp.mailer.server@gmail.com',
            ['rjdelgado@deditec.es', 'russellwallstreet@gmail.com'],
            ['rjdelgado@deditec.es'],
            reply_to=['rjdelgado@deditec.es'],
            headers={'Message-ID': 'foo'},
        )

            email.send()

            # try:
            #     print("entramos en el try")
            #     response = email.send()
            #     print("LA RESPEUSTA ES UN : ",response)
            #     if response == 0 :
            #         raise Exception("Sorry, no numbers below zero")
            #     return redirect("/contacto/?valido", )
            # except:
            #     print("entramos en el except")

            #     return redirect("/contacto/?novalido", )
            

    return render(request,"contacto/contacto.html", {"formularioContacto" : formulario_contacto} )
