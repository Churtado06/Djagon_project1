from django.contrib import admin
from GestionPedidos.models import Clientes, Articulos, Pedidos
# Register your models here.


class ClientesAdmin(admin.ModelAdmin):
    list_display=('nombre', 'direccion', 'telefono')
    #Con estos items se pueden hacer las búsquedas
    search_fields= ('nombre', 'direccion')
    # Para filtrar por columnas
    list_filter = ('nombre',)



class ArticulosAdmin(admin.ModelAdmin):
    list_display=('nombre', 'seccion', 'precio')

class PedidosAdmin(admin.ModelAdmin):
    list_display=('numero', 'fecha', 'entregado')
    list_filter=('fecha',)
    #Otro tipo de filtro para fecha "Filtro migas de pan"
    date_hierarchy='fecha'


admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)
