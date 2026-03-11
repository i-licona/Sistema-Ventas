from abc import ABC, abstractmethod
from typing import List, Optional
from ..entities import Cliente, Proveedor, Producto, Venta, Categoria


class ClienteRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Cliente]:
        pass

    @abstractmethod
    def get_by_id(self, cliente_id: int) -> Optional[Cliente]:
        pass

    @abstractmethod
    def save(self, cliente: Cliente) -> Cliente:
        pass

    @abstractmethod
    def delete(self, cliente_id: int) -> None:
        pass


class ProveedorRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Proveedor]:
        pass

    @abstractmethod
    def get_by_id(self, proveedor_id: int) -> Optional[Proveedor]:
        pass

    @abstractmethod
    def save(self, proveedor: Proveedor) -> Proveedor:
        pass

    @abstractmethod
    def delete(self, proveedor_id: int) -> None:
        pass


class ProductoRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Producto]:
        pass

    @abstractmethod
    def get_by_id(self, producto_id: int) -> Optional[Producto]:
        pass

    @abstractmethod
    def save(self, producto: Producto) -> Producto:
        pass

    @abstractmethod
    def delete(self, producto_id: int) -> None:
        pass


class VentaRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Venta]:
        pass

    @abstractmethod
    def get_by_id(self, venta_id: int) -> Optional[Venta]:
        pass

    @abstractmethod
    def save(self, venta: Venta) -> Venta:
        pass

    @abstractmethod
    def delete(self, venta_id: int) -> None:
        pass


class CategoriaRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Categoria]:
        pass

    @abstractmethod
    def get_by_id(self, categoria_id: int) -> Optional[Categoria]:
        pass

    @abstractmethod
    def save(self, categoria: Categoria) -> Categoria:
        pass

    @abstractmethod
    def delete(self, categoria_id: int) -> None:
        pass