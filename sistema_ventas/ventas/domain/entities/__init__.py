from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime


@dataclass
class Cliente:
    id: Optional[int]
    nombre: str
    email: Optional[str]
    calle: Optional[str]
    colonia: Optional[str]
    codigo_postal: Optional[str]
    ciudad: Optional[str]
    telefono: Optional[str]

    def __str__(self):
        return self.nombre


@dataclass
class Proveedor:
    id: Optional[int]
    nombre: str
    telefono: str
    calle: Optional[str]
    colonia: Optional[str]
    codigo_postal: Optional[str]
    ciudad: Optional[str]
    pagina_web: Optional[str]

    def __str__(self):
        return self.nombre


@dataclass
class Categoria:
    id: Optional[int]
    nombre: str
    descripcion: Optional[str]

    def __str__(self):
        return self.nombre


@dataclass
class Producto:
    id: Optional[int]
    nombre: str
    descripcion: Optional[str]
    precio: float
    stock: int
    categoria: Optional['Categoria'] = None

    def __str__(self):
        return self.nombre


@dataclass
class DetalleVenta:
    id: Optional[int]
    producto: Producto
    cantidad: int
    precio_unitario: float
    subtotal: float

    def __str__(self):
        return f"{self.producto.nombre} - {self.cantidad}"


@dataclass
class Venta:
    id: Optional[int]
    cliente: Cliente
    fecha: datetime
    detalles: List[DetalleVenta]
    total: float

    def __str__(self):
        return f"Venta #{self.id}"