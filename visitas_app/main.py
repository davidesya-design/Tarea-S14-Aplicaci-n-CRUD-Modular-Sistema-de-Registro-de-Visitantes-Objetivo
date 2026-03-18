"""
Punto de entrada para el sistema de registro de visitantes.
Arranca la interfaz Tkinter inyectando el servicio de visitas.
Autor: [ANDREW DAVID VALENZUELA YELA]
Fecha: [18/O3/2026]
Nota: Este archivo es el punto de entrada principal para la aplicación. No es necesario modificarlo a menos que quieras cambiar la forma en que se inicia la aplicación o agregar funcionalidades globales. La lógica principal de la aplicación se encuentra en los módulos de servicios y UI.
"""

from __future__ import annotations

import pathlib
import sys

# Permite ejecutar el archivo directamente sin instalar el paquete.
if __package__ is None or __package__ == "":
    # Agrega la carpeta raíz del proyecto al sys.path
    sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent))

from visitas_app.servicios.visita_servicio import VisitaServicio
from visitas_app.ui.app_tkinter import AppTkinter


def main() -> None:
    servicio = VisitaServicio()
    app = AppTkinter(servicio)
    app.run()


if __name__ == "__main__":
    main()
