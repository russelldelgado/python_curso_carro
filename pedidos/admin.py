from django.contrib import admin
from .models import Pedido, LineasPedido

# Register your models here.

class PedidoAdmin(admin.ModelAdmin):
    readonly_fields= ["created_at","updated_at"]


class LineaPedidoAdmin(admin.ModelAdmin):
    readonly_fields= ["created_at","updated_at"]


admin.site.register(Pedido, PedidoAdmin)
admin.site.register(LineasPedido ,LineaPedidoAdmin)




