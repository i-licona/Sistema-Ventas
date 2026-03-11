from dataclasses import dataclass
from typing import Optional


@dataclass
class Direccion:
    calle: str
    numero: str
    comunidad: str
    ciudad: str

    def __str__(self):
        return f"{self.calle} {self.numero}, {self.comunidad}, {self.ciudad}"


@dataclass
class Telefono:
    numero: str
    tipo: Optional[str] = None  # e.g., 'casa', 'trabajo', 'celular'

    def __str__(self):
        return f"{self.numero} ({self.tipo})" if self.tipo else self.numero