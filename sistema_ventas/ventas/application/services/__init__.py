from ...infrastructure.repositories.cliente_repository import DjangoClienteRepository
from ...infrastructure.repositories.proveedor_repository import DjangoProveedorRepository
from ...infrastructure.repositories.producto_repository import DjangoProductoRepository
from ...infrastructure.repositories.venta_repository import DjangoVentaRepository
from ...infrastructure.repositories.categoria_repository import DjangoCategoriaRepository
from ...infrastructure.django_models import VentaModel, DetalleVentaModel, ProductoModel


class ClienteService:
    def __init__(self):
        self.repository = DjangoClienteRepository()

    def get_all_clientes(self):
        return self.repository.get_all()

    def get_cliente_by_id(self, cliente_id):
        return self.repository.get_by_id(cliente_id)

    def create_cliente(self, cliente_data):
        return self.repository.save(cliente_data)

    def update_cliente(self, cliente_id, cliente_data):
        cliente_data.id = cliente_id
        return self.repository.save(cliente_data)

    def delete_cliente(self, cliente_id):
        return self.repository.delete(cliente_id)


class ProveedorService:
    def __init__(self):
        self.repository = DjangoProveedorRepository()

    def get_all_proveedores(self):
        return self.repository.get_all()

    def get_proveedor_by_id(self, proveedor_id):
        return self.repository.get_by_id(proveedor_id)

    def create_proveedor(self, proveedor_data):
        return self.repository.save(proveedor_data)

    def update_proveedor(self, proveedor_id, proveedor_data):
        proveedor_data.id = proveedor_id
        return self.repository.save(proveedor_data)

    def delete_proveedor(self, proveedor_id):
        return self.repository.delete(proveedor_id)


class ProductoService:
    def __init__(self):
        self.repository = DjangoProductoRepository()

    def get_all_productos(self):
        return self.repository.get_all()

    def get_producto_by_id(self, producto_id):
        return self.repository.get_by_id(producto_id)

    def create_producto(self, producto_data):
        return self.repository.save(producto_data)

    def update_producto(self, producto_id, producto_data):
        producto_data.id = producto_id
        return self.repository.save(producto_data)

    def delete_producto(self, producto_id):
        return self.repository.delete(producto_id)

    def actualizar_stock(self, producto_id, cantidad_descontar):
        """Descontar stock de un producto"""
        producto_model = ProductoModel.objects.get(id=producto_id)
        producto_model.stock -= cantidad_descontar
        if producto_model.stock < 0:
            producto_model.stock = 0
        producto_model.save()
        return True


class VentaService:
    def __init__(self):
        self.repository = DjangoVentaRepository()
        self.producto_service = ProductoService()

    def get_all_ventas(self):
        return self.repository.get_all()

    def get_venta_by_id(self, venta_id):
        return self.repository.get_by_id(venta_id)

    def create_venta(self, venta_model, detalles_data=None):
        """Crear venta con detalles y actualizar stock"""
        venta_model.save()
        total = 0
        
        if detalles_data:
            for detalle_data in detalles_data:
                producto_model = detalle_data['producto']
                cantidad = detalle_data['cantidad']
                precio_unitario = producto_model.precio
                subtotal = precio_unitario * cantidad
                
                # Crear detalle de venta
                DetalleVentaModel.objects.create(
                    venta=venta_model,
                    producto=producto_model,
                    cantidad=cantidad,
                    precio_unitario=precio_unitario,
                    subtotal=subtotal
                )
                
                # Descontar stock
                self.producto_service.actualizar_stock(producto_model.id, cantidad)
                total += float(subtotal)
        
        # Actualizar total de la venta
        venta_model.total = total
        venta_model.save()
        
        return self.repository.get_by_id(venta_model.id)

    def update_venta(self, venta_id, venta_data):
        venta_data.id = venta_id
        return self.repository.save(venta_data)

    def delete_venta(self, venta_id):
        return self.repository.delete(venta_id)

    def eliminar_detalle_venta(self, detalle_id):
        """Eliminar un detalle de venta y restaurar stock"""
        try:
            detalle = DetalleVentaModel.objects.get(id=detalle_id)
            # Restaurar stock
            self.producto_service.actualizar_stock(detalle.producto.id, -int(detalle.cantidad))
            # Actualizar total de la venta
            venta = detalle.venta
            venta.total -= float(detalle.subtotal)
            venta.save()
            # Eliminar detalle
            detalle.delete()
            return True
        except DetalleVentaModel.DoesNotExist:
            return False


class CategoriaService:
    def __init__(self):
        self.repository = DjangoCategoriaRepository()

    def get_all_categorias(self):
        return self.repository.get_all()

    def get_categoria_by_id(self, categoria_id):
        return self.repository.get_by_id(categoria_id)

    def create_categoria(self, categoria_data):
        return self.repository.save(categoria_data)

    def update_categoria(self, categoria_id, categoria_data):
        categoria_data.id = categoria_id
        return self.repository.save(categoria_data)

    def delete_categoria(self, categoria_id):
        return self.repository.delete(categoria_id)