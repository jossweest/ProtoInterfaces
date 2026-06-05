import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.dialogs import Messagebox

from src.view.widgets.DataTable import DataTable
from src.view.widgets.FormButton import FormButton, SaveButton
from src.view.widgets.LabeledEntry import LabeledEntry

from src.backend.PostgresqlConnection import PostgresqlConnection
from src.model.Autor import Autor


class AutorView(ttk.Frame):
    def __init__(self, parent, connection: PostgresqlConnection):
        super().__init__(parent)
        self.connection = connection

        self.add_model = Autor()
        self.add_model.set_connection(connection)

        self.update_model = Autor()
        self.update_model.set_connection(connection)

        self.build_ui()

    # ─────────────────────────── BUILD ────────────────────────────────────

    def build_ui(self):
        self.top_frame = ttk.Frame(self)
        self.top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self._build_left_ui()
        self._build_right_ui()
        self._build_bottom_ui()
        self._update_datatable()

    def _build_left_ui(self):
        self.left = ttk.Labelframe(self.top_frame, text="Agregar autor")
        self.left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.add_nombre = LabeledEntry(
            self.left,
            label="Nombre",
            onChange=lambda v: setattr(self.add_model, "Nombre", v),
        )
        self.add_nombre.pack(pady=5)

        SaveButton(self.left, onClick=self._insert).pack(pady=8)

    def _build_right_ui(self):
        self.right = ttk.Labelframe(self.top_frame, text="Modificar autor")
        self.right.pack(side=tk.LEFT, fill=tk.BOTH,
                        expand=True, padx=5, pady=5)

        self.update_id = LabeledEntry(self.right, label="ID Autor")
        self.update_id.entry.configure(state="readonly")
        self.update_id.pack(pady=5)

        self.update_nombre = LabeledEntry(
            self.right,
            label="Nombre",
            onChange=lambda v: setattr(self.update_model, "Nombre", v),
        )
        self.update_nombre.pack(pady=5)

        btn_frame = ttk.Frame(self.right)
        btn_frame.pack(pady=8)

        SaveButton(btn_frame, onClick=self._update).pack(side=tk.LEFT, padx=4)
        FormButton(
            btn_frame,
            text="Eliminar",
            onClick=self._delete,
            bootstyle="danger",
        ).pack(side=tk.LEFT, padx=4)

    def _build_bottom_ui(self):
        self.bottom = ttk.Labelframe(self, text="Lista de autores")
        self.bottom.pack(side=tk.TOP, fill=tk.BOTH,
                         expand=True, padx=5, pady=5)

        self.data_table = DataTable(
            self.bottom,
            columns=["idAutor", "Nombre"],
            height=7,
            onSelect=self._on_row_selected,
        )
        self.data_table.pack(fill=tk.BOTH, expand=True)

    # ─────────────────────────── VALIDACIÓN ───────────────────────────────

    def _validate_add(self) -> bool:
        nombre = self.add_nombre.get().strip()
        if not nombre:
            Messagebox.show_warning(
                "El nombre del autor es obligatorio.", title="Validación")
            return False
        return True

    def _validate_update(self) -> bool:
        if not self.update_id.get():
            Messagebox.show_warning(
                "Selecciona un registro de la tabla primero.", title="Validación")
            return False

        nombre = self.update_nombre.get().strip()
        if not nombre:
            Messagebox.show_warning(
                "El nombre del autor es obligatorio.", title="Validación")
            return False

        return True

    # ─────────────────────────── ACCIONES CRUD ────────────────────────────

    def _insert(self):
        if not self._validate_add():
            return
        try:
            self.add_model.Nombre = self.add_nombre.get().strip()
            self.add_model.insert()
            self._update_datatable()
            self.add_nombre.clear()
            Messagebox.show_info(
                "Autor agregado correctamente.", title="Éxito")
        except Exception as e:
            Messagebox.show_error(f"Error al insertar:\n{e}", title="Error")

    def _update(self):
        if not self._validate_update():
            return
        try:
            self.update_model.Nombre = self.update_nombre.get().strip()
            self.update_model.update()
            self._update_datatable()
            Messagebox.show_info(
                "Autor actualizado correctamente.", title="Éxito")
        except Exception as e:
            Messagebox.show_error(f"Error al actualizar:\n{e}", title="Error")

    def _delete(self):
        if not self.update_id.get():
            Messagebox.show_warning(
                "Selecciona un registro de la tabla primero.", title="Validación")
            return

        confirm = Messagebox.yesno(
            f"¿Eliminar al autor '{self.update_nombre.get()}' (ID {self.update_id.get()})?",
            title="Confirmar eliminación",
        )
        if confirm not in ["Yes", "Sí", "Ja"]:
            return

        try:
            self.update_model.delete()
            self._update_datatable()
            self._clear_right_form()
            Messagebox.show_info(
                "Autor eliminado correctamente.", title="Éxito")
        except Exception as e:
            Messagebox.show_error(f"Error al eliminar:\n{e}", title="Error")

    # ─────────────────────────── TABLA ────────────────────────────────────

    def _update_datatable(self):
        self.data_table.clear()
        tmp = Autor()
        tmp.set_connection(self.connection)
        self.data_table.insertMany(
            [(autor.id, autor.Nombre) for autor in tmp.select()]
        )

    def _on_row_selected(self, values: tuple):
        """Llena el formulario derecho con los datos de la fila seleccionada."""
        if not values:
            return

        id_autor, nombre = values

        self.update_model.id = int(id_autor)
        self.update_model.Nombre = nombre

        self.update_id.set(id_autor)
        self.update_nombre.set(nombre)

    def _clear_right_form(self):
        """Limpia el formulario derecho tras una eliminación."""
        self.update_id.set("")
        self.update_nombre.clear()

        self.update_model = Autor()
        self.update_model.set_connection(self.connection)
