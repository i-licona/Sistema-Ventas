from django.contrib import admin

# Register your models here.
from .models import Cliente, Producto, Venta, DetalleVenta

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(DetalleVenta)