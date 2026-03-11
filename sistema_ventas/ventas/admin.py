from django.contrib import admin
from .infrastructure.django_models import ClienteModel, ProveedorModel, ProductoModel, VentaModel, DetalleVentaModel

admin.site.register(ClienteModel)
admin.site.register(ProveedorModel)
admin.site.register(ProductoModel)
admin.site.register(VentaModel)
admin.site.register(DetalleVentaModel)