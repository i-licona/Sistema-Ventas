from typing import List, Optional
from django.core.exceptions import ObjectDoesNotExist
from ...domain.repositories import ProductoRepository
from ...domain.entities import Producto
from ..django_models import ProductoModel


class DjangoProductoRepository(ProductoRepository):
    def get_all(self) -> List[Producto]:
        productos_models = ProductoModel.objects.all()
        return [self._model_to_entity(producto_model) for producto_model in productos_models]

    def get_by_id(self, producto_id: int) -> Optional[Producto]:
        try:
            producto_model = ProductoModel.objects.get(id=producto_id)
            return self._model_to_entity(producto_model)
        except ObjectDoesNotExist:
            return None

    def save(self, producto_model: ProductoModel) -> Producto:
        if producto_model.pk:
            producto_model.save(update_fields=['nombre', 'descripcion', 'precio', 'stock', 'categoria'])
        else:
            producto_model.save()
        return self._model_to_entity(producto_model)

    def delete(self, producto_id: int) -> None:
        ProductoModel.objects.filter(id=producto_id).delete()

    def _model_to_entity(self, producto_model: ProductoModel) -> Producto:
        categoria = None
        if producto_model.categoria:
            from .categoria_repository import DjangoCategoriaRepository
            categoria_repo = DjangoCategoriaRepository()
            categoria = categoria_repo.get_by_id(producto_model.categoria_id)
        
        return Producto(
            id=producto_model.id,
            nombre=producto_model.nombre,
            descripcion=producto_model.descripcion,
            precio=float(producto_model.precio),
            stock=producto_model.stock,
            categoria=categoria
        )