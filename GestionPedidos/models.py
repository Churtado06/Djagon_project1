from django.db import models



"""
from GestionPedidos.models import Clientes
cliente2 = Clientes(nombre='Cristian Hurtado',direccion='Aida Lucia', email='cristianhurtado06@gmail.com',telefono='301781')
cliente2.save()

cliente3 = Clientes.objects.create(nombre='Lewis',direccion='Monaco', email='lh@gmai.com',telefono='625456')
#Para actualizar
cliente3.email='lh@gmail.com'
cliente3.save()
#Pra borrar 
eliminar = Clientes.objects.get(id=3)
eliminar.delete()

"""

# CADA VEZ QUE SE HAGA UN CAMBIO EN EL MODELO HAY QUE HACER:
# python manage.py makemigrations
# python manage.py migrate

# Create your models here.

#La base de datos tendrá tres tablas y cada tabla tendrá 3 columnas
class Clientes(models.Model):
    #Se indica que tipo de dato se va a almacenar 
    nombre=models.CharField(max_length=30)    # Se va a agregar texto
    #Con verbose_name se elige como va a aprecer en el panel de administracion
    direccion=models.CharField(max_length=50, verbose_name='Dirección actual')
    #Esto se hace para hacer que sea opcional al momento de llenarlo en el panel de administración
    email = models.EmailField(blank=True, null= True)               #Solo se pueden especificar direcciones de email validas
    telefono= models.CharField(max_length=7)  # 

    def __str__(self):
        return self.nombre 

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)    # Tipo Char: Texto
    seccion=models.CharField(max_length=20)   # Tipo char: Texto
    precio= models.IntegerField() #Campo de tipo entero

class Pedidos(models.Model):
    numero= models.IntegerField()   # Números enteros
    fecha= models.DateField()       #Especifico para fechas
    entregado=models.BooleanField()  #Booleano
 