"""
Servicio encargado de la lógica CRUD de visitantes.
Gestiona internamente la lista en memoria.
"""

from __future__ import annotations

from typing import List

from visitas_app.modelos.visitante import Visitante


class VisitaServicio:
    def __init__(self) -> None:
        self._visitantes: List[Visitante] = []

    def agregar(self, visitante: Visitante) -> None:
        """Agrega un visitante si la cédula no existe."""
        if any(v.cedula == visitante.cedula for v in self._visitantes):
            raise ValueError("Ya existe un visitante con esa cédula.")
        self._visitantes.append(visitante)

    def eliminar(self, cedula: str) -> None:
        """Elimina por cédula; lanza error si no se encuentra."""
        for idx, visitante in enumerate(self._visitantes):
            if visitante.cedula == cedula:
                del self._visitantes[idx]
                return
        raise ValueError("No se encontró el visitante a eliminar.")

    def obtener_todos(self) -> List[Visitante]:
        """Devuelve una copia de la lista para evitar modificaciones externas."""
        return list(self._visitantes)
