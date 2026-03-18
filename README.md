# Tarea s14: Aplicación CRUD Modular – Sistema de Registro de Visitantes

ANDREW DAVID VALENZUELA YELA

Objetivo

Aplicación de escritorio desarrollada en Python con Tkinter para la gestión de visitantes. Implementa operaciones CRUD en memoria y sigue una arquitectura modular por capas.

## Estructura del proyecto

visitas_app/

├── main.py

├── modelos/

│   └── visitante.py

├── servicios/

│   └── visita_servicio.py

└── ui/
    └── app_tkinter.py

## Requisitos

- Python 3.10 o superior
- Tkinter (incluido en la instalación estándar de Python)

## Ejecución

Desde la raíz del repositorio:

python -m visitas_app.main

O ejecutando directamente desde el paquete:

cd visitas_app
python main.py

## Funcionalidades

- Registro de visitantes (cédula, nombre, motivo)
- Visualización de registros en tabla (ttk.Treeview)
- Eliminación de registros seleccionados
- Limpieza automática del formulario tras cada acción

## Notas

- Los datos se almacenan únicamente en memoria (sin persistencia en disco)
- La interfaz utiliza inyección de dependencias para mantener la separación de capas
