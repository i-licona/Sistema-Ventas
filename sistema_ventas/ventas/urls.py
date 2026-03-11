from django.urls import path
from . import views

urlpatterns = [
    # inicio
    path('', views.inicio, name='inicio'),
    
    # Categorías
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/crear/', views.crear_categoria, name='crear_categoria'),
    path('categorias/<int:categoria_id>/editar/', views.editar_categoria, name='editar_categoria'),
    path('categorias/<int:categoria_id>/eliminar/', views.eliminar_categoria, name='eliminar_categoria'),
    
    # Productos
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    path('productos/<int:producto_id>/editar/', views.editar_producto, name='editar_producto'),
    path('productos/<int:producto_id>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
    
    # Clientes
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/crear/', views.crear_cliente, name='crear_cliente'),
    path('clientes/<int:cliente_id>/editar/', views.editar_cliente, name='editar_cliente'),
    path('clientes/<int:cliente_id>/eliminar/', views.eliminar_cliente, name='eliminar_cliente'),
    
    # Proveedores
    path('proveedores/', views.lista_proveedores, name='lista_proveedores'),
    path('proveedores/crear/', views.crear_proveedor, name='crear_proveedor'),
    path('proveedores/<int:proveedor_id>/editar/', views.editar_proveedor, name='editar_proveedor'),
    path('proveedores/<int:proveedor_id>/eliminar/', views.eliminar_proveedor, name='eliminar_proveedor'),
    
    # Ventas
    path('ventas/', views.lista_ventas, name='lista_ventas'),
    path('ventas/crear/', views.crear_venta, name='crear_venta'),
    path('ventas/<int:venta_id>/editar/', views.editar_venta, name='editar_venta'),
    path('ventas/<int:venta_id>/detalle/', views.detalle_venta, name='detalle_venta'),
    path('ventas/<int:venta_id>/eliminar/', views.eliminar_venta, name='eliminar_venta'),
    path('ventas/<int:venta_id>/guardar/', views.guardar_venta, name='guardar_venta'),
    path('ventas/<int:venta_id>/agregar-producto/', views.agregar_producto_venta, name='agregar_producto_venta'),
    path('ventas/detalle/<int:detalle_id>/eliminar/', views.eliminar_detalle_venta, name='eliminar_detalle_venta'),
]