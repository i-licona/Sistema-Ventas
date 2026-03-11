from typing import List, Optional
from django.core.exceptions import ObjectDoesNotExist
from ...domain.repositories import VentaRepository
from ...domain.entities import Venta
from ..django_models import VentaModel, DetalleVentaModel


class DjangoVentaRepository(VentaRepository):
    def get_all(self) -> List[Venta]:
        ventas_models = VentaModel.objects.all()
        return [self._model_to_entity(venta_model) for venta_model in ventas_models]

    def get_by_id(self, venta_id: int) -> Optional[Venta]:
        try:
            venta_model = VentaModel.objects.get(id=venta_id)
            return self._model_to_entity(venta_model)
        except ObjectDoesNotExist:
            return None

    def save(self, venta_model: VentaModel) -> Venta:
        if venta_model.pk:
            venta_model.save(update_fields=['cliente', 'total'])
        else:
            venta_model.save()
        return self._model_to_entity(venta_model)

    def delete(self, venta_id: int) -> None:
        VentaModel.objects.filter(id=venta_id).delete()

    def _model_to_entity(self, venta_model: VentaModel) -> Venta:
        from ...domain.value_objects import Telefono
        from ...domain.entities import DetalleVenta
        from .cliente_repository import DjangoClienteRepository
        
        cliente_repo = DjangoClienteRepository()
        cliente = cliente_repo.get_by_id(venta_model.cliente_id)
        
        detalles = []
        for detalle_model in venta_model.detalles.all():
            detalle = DetalleVenta(
                id=detalle_model.id,
                producto=self._producto_model_to_entity(detalle_model.producto),
                cantidad=detalle_model.cantidad,
                precio_unitario=float(detalle_model.precio_unitario),
                subtotal=float(detalle_model.subtotal)
            )
            detalles.append(detalle)
        
        return Venta(
            id=venta_model.id,
            cliente=cliente,
            fecha=venta_model.fecha,
            detalles=detalles,
            total=float(venta_model.total)
        )
    
    def _producto_model_to_entity(self, producto_model):
        from ...domain.entities import Producto
        return Producto(
            id=producto_model.id,
            nombre=producto_model.nombre,
            descripcion=producto_model.descripcion,
            precio=float(producto_model.precio),
            stock=producto_model.stock
        )