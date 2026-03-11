from typing import List, Optional
from django.core.exceptions import ObjectDoesNotExist
from ...domain.repositories import CategoriaRepository
from ...domain.entities import Categoria
from ..django_models import CategoriaModel


class DjangoCategoriaRepository(CategoriaRepository):
    def get_all(self) -> List[Categoria]:
        categorias_models = CategoriaModel.objects.all()
        return [self._model_to_entity(categoria_model) for categoria_model in categorias_models]

    def get_by_id(self, categoria_id: int) -> Optional[Categoria]:
        try:
            categoria_model = CategoriaModel.objects.get(id=categoria_id)
            return self._model_to_entity(categoria_model)
        except ObjectDoesNotExist:
            return None

    def save(self, categoria_model: CategoriaModel) -> Categoria:
        if categoria_model.pk:
            categoria_model.save(update_fields=['nombre', 'descripcion'])
        else:
            categoria_model.save()
        return self._model_to_entity(categoria_model)

    def delete(self, categoria_id: int) -> None:
        CategoriaModel.objects.filter(id=categoria_id).delete()

    def _model_to_entity(self, categoria_model: CategoriaModel) -> Categoria:
        return Categoria(
            id=categoria_model.id,
            nombre=categoria_model.nombre,
            descripcion=categoria_model.descripcion
        )
