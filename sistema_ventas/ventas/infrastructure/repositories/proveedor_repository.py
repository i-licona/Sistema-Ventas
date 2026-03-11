from typing import List, Optional
from django.core.exceptions import ObjectDoesNotExist
from ...domain.repositories import ProveedorRepository
from ...domain.entities import Proveedor
from ..django_models import ProveedorModel


class DjangoProveedorRepository(ProveedorRepository):
    def get_all(self) -> List[Proveedor]:
        proveedores_models = ProveedorModel.objects.all()
        return [self._model_to_entity(proveedor_model) for proveedor_model in proveedores_models]

    def get_by_id(self, proveedor_id: int) -> Optional[Proveedor]:
        try:
            proveedor_model = ProveedorModel.objects.get(id=proveedor_id)
            return self._model_to_entity(proveedor_model)
        except ObjectDoesNotExist:
            return None

    def save(self, proveedor_model: ProveedorModel) -> Proveedor:
        if proveedor_model.pk:
            proveedor_model.save(update_fields=['nombre', 'telefono', 'pagina_web', 'calle', 'colonia', 'codigo_postal', 'ciudad'])
        else:
            proveedor_model.save()
        return self._model_to_entity(proveedor_model)

    def delete(self, proveedor_id: int) -> None:
        ProveedorModel.objects.filter(id=proveedor_id).delete()

    def _model_to_entity(self, proveedor_model: ProveedorModel) -> Proveedor:
        return Proveedor(
            id=proveedor_model.id,
            nombre=proveedor_model.nombre,
            telefono=proveedor_model.telefono,
            calle=proveedor_model.calle,
            colonia=proveedor_model.colonia,
            codigo_postal=proveedor_model.codigo_postal,
            ciudad=proveedor_model.ciudad,
            pagina_web=proveedor_model.pagina_web
        )