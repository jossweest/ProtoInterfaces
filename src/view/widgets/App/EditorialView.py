import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox
from typing import Optional

from src.model.Editorial import Editorial
from src.view.widgets.LabeledEntry import LabeledEntry
from src.view.widgets.FormButton import SaveButton, ClearButton
from src.view.widgets.DataTable import DataTable


class EditorialView(ttk.Frame):
    def __init__(self, parent: tk.Widget, modelo: Editorial, **kwargs):
        super().__init__(parent, **kwargs)

        self._modelo = modelo
        self._id_editando: Optional[int] = None   # None → modo crear

        self._build_ui()
        self._load_table()

    def _build_ui(self):
        ttk.Label(
            self,
            text="Editoriales",
            font=("Arial", 16, "bold"),
        ).pack(anchor="w", padx=20, pady=(15, 0))

        ttk.Separator(self).pack(fill="x", padx=20, pady=8)

        form = ttk.LabelFrame(self, text="Datos de la editorial", padding=12)
        form.pack(fill="x", padx=20, pady=(0, 10))

        self._campo_nombre = LabeledEntry(
            form,
            label="Nombre",
            width=40,
            onChange=lambda v: setattr(self._modelo, "Nombre", v),
        )
        self._campo_nombre.pack(fill="x")

        btn_row = ttk.Frame(form)
        btn_row.pack(fill="x", pady=(10, 0))

        self._btn_guardar = SaveButton(
            btn_row,
            text="Guardar",
            onClick=self._guardar,
            bootstyle="primary",
        )
        self._btn_guardar.pack(side="left", padx=(0, 6))

        self._btn_eliminar = ttk.Button(
            btn_row,
            text="Eliminar",
            bootstyle="danger-outline",
            command=self._eliminar,
            state="disabled",
        )
        self._btn_eliminar.pack(side="left", padx=(0, 6))

        ClearButton(
            btn_row,
            onClick=self._limpiar,
            bootstyle="secondary-outline",
        ).pack(side="left")

        ttk.Label(
            self,
            text="Registros guardados",
            font=("Arial", 11),
        ).pack(anchor="w", padx=20, pady=(4, 0))

        self._tabla = DataTable(
            self,
            columns=["ID", "Nombre"],
            height=10,
            onSelect=self._on_seleccionar,
        )
        self._tabla.setColumnWidth("ID", 60)
        self._tabla.setColumnWidth("Nombre", 340)
        self._tabla.pack(fill="both", expand=True, padx=20, pady=(4, 15))

    def _modo_crear(self):
        """Resetea la UI al estado inicial (sin selección)."""
        self._id_editando = None
        self._modelo.idEditorial = 0
        self._modelo.Nombre = ""
        self._campo_nombre.clear()
        self._btn_guardar.config(text="Guardar")
        self._btn_eliminar.config(state="disabled")

    def _modo_editar(self, id_editorial: int, nombre: str):
        """Carga los datos de la fila seleccionada en el formulario."""
        self._id_editando = id_editorial
        self._modelo.idEditorial = id_editorial
        self._modelo.Nombre = nombre
        self._campo_nombre.set(nombre)
        self._btn_guardar.config(text="Actualizar")
        self._btn_eliminar.config(state="normal")

    # ──────────────────────────────────────────────────────────────────
    # Callbacks
    # ──────────────────────────────────────────────────────────────────

    def _on_seleccionar(self, row: Optional[tuple]):
        """Dispara DataTable.onSelect: carga la fila en el formulario."""
        if not row:
            return
        self._modo_editar(id_editorial=int(row[0]), nombre=row[1])

    def _guardar(self):
        """Inserta o actualiza según el estado actual."""
        nombre = self._modelo.Nombre.strip()
        if not nombre:
            Messagebox.show_warning(
                "El nombre de la editorial no puede estar vacío.",
                title="Campo requerido",
            )
            return

        try:
            if self._id_editando is None:
                self._modelo.insert()
                Messagebox.show_info(
                    f"Editorial '{nombre}' guardada correctamente.",
                    title="Guardado",
                )
            else:
                self._modelo.update()
                Messagebox.show_info(
                    f"Editorial '{nombre}' actualizada correctamente.",
                    title="Actualizado",
                )

            self._limpiar()

        except Exception as e:
            Messagebox.show_error(
                f"No se pudo guardar: {e}",
                title="Error",
            )

    def _eliminar(self):
        """Elimina la editorial seleccionada tras confirmación."""
        if self._id_editando is None:
            return

        confirmar = Messagebox.yesno(
            message=f"¿Eliminar la editorial '{self._modelo.Nombre}'?\nEsta acción no se puede deshacer.",
            title="Confirmar eliminación",
        )
        if confirmar != "Yes":
            return

        try:
            self._modelo.delete()
            Messagebox.show_info(
                f"Editorial eliminada correctamente.",
                title="Eliminado",
            )
            self._limpiar()

        except Exception as e:
            Messagebox.show_error(
                f"No se pudo eliminar: {e}",
                title="Error",
            )

    def _limpiar(self):
        """Vuelve al modo crear y recarga la tabla."""
        self._modo_crear()
        self._cargar_tabla()

    # ──────────────────────────────────────────────────────────────────
    # Tabla
    # ──────────────────────────────────────────────────────────────────

    def _cargar_tabla(self):
        """Lee todos los registros del modelo y los muestra en la tabla."""
        self._tabla.clear()
        try:
            for editorial in self._modelo.select():
                self._tabla.insert((editorial.idEditorial, editorial.Nombre))
        except Exception as e:
            # Posible bug en Editorial.select(): `yield self(...)` debería
            # ser `yield self.__class__(...)`. Corrige el modelo si ocurre.
            print(f"[EditorialView] Error al cargar tabla: {e}")


# ──────────────────────────────────────────────────────────────────────
# Prueba rápida (sin BD real)
# ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    from unittest.mock import MagicMock, patch

    # Mock del modelo para probar la UI sin conexión a BD
    modelo_mock = MagicMock(spec=Editorial)
    modelo_mock.Nombre = ""
    modelo_mock.idEditorial = 0
    modelo_mock.select.return_value = [
        MagicMock(idEditorial=1, Nombre="Pollito Editorial"),
        MagicMock(idEditorial=2, Nombre="Libros Medianoche"),
        MagicMock(idEditorial=3, Nombre="Editorial Cuervo"),
    ]

    root = ttk.Window(themename="yeti")
    root.title("EditorialView – prueba")
    root.geometry("700x550")

    vista = EditorialView(root, modelo=modelo_mock)
    vista.pack(fill="both", expand=True)

    root.mainloop()
