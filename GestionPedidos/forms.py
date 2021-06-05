from django import forms

class FormularioContacto(forms.form):
    #Especificar los campos que va a tener el formulario

    asunto= forms.CharField()
    email = forms.EmailField()
    mensaje= forms.CharField()