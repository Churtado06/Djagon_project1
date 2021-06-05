from django.shortcuts import render
from django.http import HttpResponse
from GestionPedidos.models import Articulos
from GestionPedidos.forms import FormularioContacto
# Create your views here.

def busqueda_productos(request):

    return render(request, 'busqueda_productos.html')

def buscar(request):
    
    if request.GET['producto']:
        #mensaje='Artículo buscado: %r' %request.GET['producto']
        producto= request.GET['producto']
        
        #Hacer que la entrada no tenga más de 20 caracteres
        if len(producto)>20:
            mensaje= 'No se ha encontrado el producto'
        else:
        # __icontains es como el LIKE en sql
            articulos= Articulos.objects.filter(nombre__icontains= producto)

            return render(request,'resultado_busqueda.html', {'articulos': articulos, 'query': producto})
    else:
        mensaje= 'No has seleccionado ningún artículo'

    return HttpResponse(mensaje)
"""
def contacto1(request):

    if request.method == 'POST':

        return render (request, 'gracias.html')

    return render(request, 'contacto.html')
"""
def contacto (request):
    if request.method == 'POST': #Si el usuario a pulsado el boton de enviar
        formulario=FormularioContacto(request.POST)

        if formulario.is_valid():
            informacion=formulario.cleaned_data

            send_mail(informacion['asunto'], informacion['mensaje'], informacion.get('email','')['cristianhurtado06@gmail.com']) 

            return render(request, 'gracias.html')
        else:
            formulario = FormularioContacto()
    