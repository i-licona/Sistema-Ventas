from typing import List, Optional
from django.core.exceptions import ObjectDoesNotExist
from ...domain.repositories import ClienteRepository
from ...domain.entities import Cliente
from ..django_models import ClienteModel


class DjangoClienteRepository(ClienteRepository):
    def get_all(self) -> List[Cliente]:
        clientes_models = ClienteModel.objects.all()
        return [self._model_to_entity(cliente_model) for cliente_model in clientes_models]

    def get_by_id(self, cliente_id: int) -> Optional[Cliente]:
        try:
            cliente_model = ClienteModel.objects.get(id=cliente_id)
            return self._model_to_entity(cliente_model)
        except ObjectDoesNotExist:
            return None

    def save(self, cliente_model: ClienteModel) -> Cliente:
        if cliente_model.pk:
            cliente_model.save(update_fields=['nombre', 'email', 'calle', 'colonia', 'codigo_postal', 'ciudad', 'telefono'])
        else:
            cliente_model.save()
        return self._model_to_entity(cliente_model)

    def delete(self, cliente_id: int) -> None:
        ClienteModel.objects.filter(id=cliente_id).delete()

    def _model_to_entity(self, cliente_model: ClienteModel) -> Cliente:
        return Cliente(
            id=cliente_model.id,
            nombre=cliente_model.nombre,
            email=cliente_model.email,
            calle=cliente_model.calle,
            colonia=cliente_model.colonia,
            codigo_postal=cliente_model.codigo_postal,
            ciudad=cliente_model.ciudad,
            telefono=cliente_model.telefono
        )