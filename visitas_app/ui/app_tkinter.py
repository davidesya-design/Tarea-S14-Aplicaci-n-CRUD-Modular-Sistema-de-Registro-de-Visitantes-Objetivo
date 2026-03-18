"""
Interfaz gráfica construida con Tkinter.
Recibe el servicio por inyección de dependencias.
"""

import tkinter as tk
from tkinter import messagebox, ttk

from visitas_app.modelos.visitante import Visitante
from visitas_app.servicios.visita_servicio import VisitaServicio


class AppTkinter:
    def __init__(self, servicio: VisitaServicio) -> None:
        self.servicio = servicio
        self.root = tk.Tk()
        self.root.title("Registro de Visitantes")
        self.root.resizable(False, False)

        self._crear_widgets()
        self._configurar_layout()

    def _crear_widgets(self) -> None:
        # Entradas
        self.cedula_var = tk.StringVar()
        self.nombre_var = tk.StringVar()
        self.motivo_var = tk.StringVar()

        self.lbl_cedula = ttk.Label(self.root, text="Cédula:")
        self.entry_cedula = ttk.Entry(self.root, textvariable=self.cedula_var, width=30)

        self.lbl_nombre = ttk.Label(self.root, text="Nombre completo:")
        self.entry_nombre = ttk.Entry(self.root, textvariable=self.nombre_var, width=30)

        self.lbl_motivo = ttk.Label(self.root, text="Motivo de la visita:")
        self.entry_motivo = ttk.Entry(self.root, textvariable=self.motivo_var, width=30)

        # Botones
        self.btn_registrar = ttk.Button(self.root, text="Registrar", command=self._registrar)
        self.btn_eliminar = ttk.Button(self.root, text="Eliminar seleccionado", command=self._eliminar)
        self.btn_limpiar = ttk.Button(self.root, text="Limpiar campos", command=self._limpiar_formulario)

        # Tabla
        columnas = ("cedula", "nombre", "motivo")
        self.tree = ttk.Treeview(self.root, columns=columnas, show="headings", height=8)
        self.tree.heading("cedula", text="Cédula")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("motivo", text="Motivo")
        for col, ancho in zip(columnas, (120, 180, 220)):
            self.tree.column(col, width=ancho, anchor=tk.W)

        self.scroll_y = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scroll_y.set)

    def _configurar_layout(self) -> None:
        pad = {"padx": 8, "pady": 4}

        self.lbl_cedula.grid(row=0, column=0, sticky="w", **pad)
        self.entry_cedula.grid(row=0, column=1, **pad)

        self.lbl_nombre.grid(row=1, column=0, sticky="w", **pad)
        self.entry_nombre.grid(row=1, column=1, **pad)

        self.lbl_motivo.grid(row=2, column=0, sticky="w", **pad)
        self.entry_motivo.grid(row=2, column=1, **pad)

        self.btn_registrar.grid(row=3, column=0, **pad)
        self.btn_eliminar.grid(row=3, column=1, sticky="w", **pad)
        self.btn_limpiar.grid(row=3, column=1, sticky="e", **pad)

        self.tree.grid(row=4, column=0, columnspan=2, sticky="nsew", padx=(8, 0), pady=(8, 4))
        self.scroll_y.grid(row=4, column=2, sticky="ns", padx=(0, 8), pady=(8, 4))

        self.root.grid_columnconfigure(1, weight=1)

    def _registrar(self) -> None:
        cedula = self.cedula_var.get().strip()
        nombre = self.nombre_var.get().strip()
        motivo = self.motivo_var.get().strip()

        if not cedula or not nombre or not motivo:
            messagebox.showwarning("Campos incompletos", "Todos los campos son obligatorios.")
            return

        try:
            visitante = Visitante(cedula, nombre, motivo)
            self.servicio.agregar(visitante)
        except ValueError as exc:
            messagebox.showerror("Error", str(exc))
            return

        self._refrescar_tabla()
        self._limpiar_formulario()
        messagebox.showinfo("Éxito", "Visitante registrado correctamente.")

    def _eliminar(self) -> None:
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Sin selección", "Seleccione un registro en la tabla.")
            return

        item_id = seleccionado[0]
        cedula = self.tree.item(item_id, "values")[0]

        try:
            self.servicio.eliminar(cedula)
        except ValueError as exc:
            messagebox.showerror("Error", str(exc))
            return

        self._refrescar_tabla()
        self._limpiar_formulario()
        messagebox.showinfo("Eliminado", "Registro eliminado.")

    def _limpiar_formulario(self) -> None:
        self.cedula_var.set("")
        self.nombre_var.set("")
        self.motivo_var.set("")
        for item in self.tree.selection():
            self.tree.selection_remove(item)

    def _refrescar_tabla(self) -> None:
        self.tree.delete(*self.tree.get_children())
        for visitante in self.servicio.obtener_todos():
            self.tree.insert("", tk.END, values=visitante.to_tuple())

    def run(self) -> None:
        self.root.mainloop()
