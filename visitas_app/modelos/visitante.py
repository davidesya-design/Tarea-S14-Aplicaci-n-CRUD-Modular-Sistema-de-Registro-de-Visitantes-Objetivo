"""
Modelo de datos para un visitante.
"""

from dataclasses import dataclass


@dataclass
class Visitante:
    cedula: str
    nombre: str
    motivo: str

    def to_tuple(self) -> tuple[str, str, str]:
        """Devuelve los datos listos para mostrarse en la tabla."""
        return self.cedula, self.nombre, self.motivo
