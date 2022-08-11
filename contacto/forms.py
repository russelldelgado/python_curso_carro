from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label="nombre" , required=True , max_length=100)
    email = forms.CharField(label="email", required=True , max_length=100)
    contenido = forms.CharField(label="contenido", required=False , max_length=500 , widget=forms.Textarea)
