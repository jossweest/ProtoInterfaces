import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.dialogs import Messagebox

from src.view.widgets.DataTable import DataTable
from src.view.widgets.FormButton import FormButton, SaveButton
from src.view.widgets.LabeledEntry import LabeledEntry

from src.backend.PostgresqlConnection import PostgresqlConnection
from src.model.Cliente import Cliente


class ClienteView(ttk.Frame):
    def __init__(self, parent, connection: PostgresqlConnection):
        super().__init__(parent)
        self.connection = connection

        self.add_model = Cliente()
        self.add_model.set_connection(connection)

        self.update_model = Cliente()
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
        self.left = ttk.Labelframe(self.top_frame, text="Agregar datos")
        self.left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.add_nombre = LabeledEntry(
            self.left,
            label="Nombre",
            onChange=lambda v: setattr(self.add_model, "Nombre", v),
        )
        self.add_nombre.pack()

        self.add_apellidos = LabeledEntry(
            self.left,
            label="Apellidos",
            onChange=lambda v: setattr(self.add_model, "Apellidos", v),
        )
        self.add_apellidos.pack()

        self.add_correo = LabeledEntry(
            self.left,
            label="Correo electrónico",
            onChange=lambda v: setattr(self.add_model, "CorreoElectronico", v),
        )
        self.add_correo.pack()

        self.add_celular = LabeledEntry(
            self.left,
            label="Número de celular",
            onChange=lambda v: setattr(self.add_model, "NumCelular", v),
        )
        self.add_celular.pack()

        SaveButton(self.left, onClick=self._insert).pack(pady=8)

    def _build_right_ui(self):
        self.right = ttk.Labelframe(self.top_frame, text="Modificar datos")
        self.right.pack(side=tk.LEFT, fill=tk.BOTH,
                        expand=True, padx=5, pady=5)

        # ID (solo lectura, se llena al seleccionar fila)
        self.update_id = LabeledEntry(self.right, label="Id Cliente")
        self.update_id.entry.configure(state="readonly")
        self.update_id.pack()

        # Campos editables
        self.update_nombre = LabeledEntry(self.right, label="Nombre")
        self.update_nombre.pack()

        self.update_apellidos = LabeledEntry(self.right, label="Apellidos")
        self.update_apellidos.pack()

        self.update_correo = LabeledEntry(
            self.right, label="Correo electrónico")
        self.update_correo.pack()

        self.update_celular = LabeledEntry(
            self.right, label="Número de celular")
        self.update_celular.pack()

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
        self.bottom = ttk.Labelframe(self, text="Consultar datos")
        self.bottom.pack(side=tk.TOP, fill=tk.BOTH,
                         expand=True, padx=5, pady=5)

        self.data_table = DataTable(
            self.bottom,
            columns=["IdCliente", "Nombre", "Apellidos",
                     "CorreoElectronico", "NumCelular"],
            height=7,
            onSelect=self._on_row_selected,
        )
        self.data_table.pack(fill=tk.BOTH, expand=True)

    # ─────────────────────────── VALIDACIÓN ───────────────────────────────

    def _validate_add(self) -> bool:
        if not self.add_nombre.get().strip():
            Messagebox.show_warning(
                "El nombre es obligatorio.", title="Validación")
            return False
        if not self.add_apellidos.get().strip():
            Messagebox.show_warning(
                "Los apellidos son obligatorios.", title="Validación")
            return False
        if not self.add_correo.get().strip():
            Messagebox.show_warning(
                "El correo electrónico es obligatorio.", title="Validación")
            return False
        if not self.add_celular.get().strip():
            Messagebox.show_warning(
                "El número de celular es obligatorio.", title="Validación")
            return False
        return True

    def _validate_update(self) -> bool:
        if not self.update_id.get():
            Messagebox.show_warning(
                "Selecciona un registro de la tabla primero.", title="Validación"
            )
            return False
        if not self.update_nombre.get().strip():
            Messagebox.show_warning(
                "El nombre es obligatorio.", title="Validación")
            return False
        if not self.update_apellidos.get().strip():
            Messagebox.show_warning(
                "Los apellidos son obligatorios.", title="Validación")
            return False
        if not self.update_correo.get().strip():
            Messagebox.show_warning(
                "El correo electrónico es obligatorio.", title="Validación")
            return False
        if not self.update_celular.get().strip():
            Messagebox.show_warning(
                "El número de celular es obligatorio.", title="Validación")
            return False
        return True

    # ─────────────────────────── ACCIONES CRUD ────────────────────────────

    def _insert(self):
        if not self._validate_add():
            return
        try:
            self.add_model.Nombre = self.add_nombre.get().strip()
            self.add_model.Apellidos = self.add_apellidos.get().strip()
            self.add_model.CorreoElectronico = self.add_correo.get().strip()
            self.add_model.NumCelular = self.add_celular.get().strip()
            self.add_model.insert()
            self._update_datatable()
            self._clear_add_form()
            Messagebox.show_info(
                "Cliente agregado correctamente.", title="Éxito")
        except Exception as e:
            Messagebox.show_error(f"Error al insertar:\n{e}", title="Error")

    def _update(self):
        if not self._validate_update():
            return
        try:
            self.update_model.Nombre = self.update_nombre.get().strip()
            self.update_model.Apellidos = self.update_apellidos.get().strip()
            self.update_model.CorreoElectronico = self.update_correo.get().strip()
            self.update_model.NumCelular = self.update_celular.get().strip()
            self.update_model.update()
            self._update_datatable()
            Messagebox.show_info(
                "Cliente actualizado correctamente.", title="Éxito")
        except Exception as e:
            Messagebox.show_error(f"Error al actualizar:\n{e}", title="Error")

    def _delete(self):
        if not self.update_id.get():
            Messagebox.show_warning(
                "Selecciona un registro de la tabla primero.", title="Validación"
            )
            return

        confirm = Messagebox.yesno(
            f"¿Eliminar al cliente {self.update_id.get()} - {self.update_nombre.get()} {self.update_apellidos.get()}?",
            title="Confirmar eliminación",
        )
        if confirm not in ["Yes", "Sí", "Ja"]:
            return

        try:
            self.update_model.delete()
            self._update_datatable()
            self._clear_right_form()
            Messagebox.show_info(
                "Cliente eliminado correctamente.", title="Éxito")
        except Exception as e:
            Messagebox.show_error(f"Error al eliminar:\n{e}", title="Error")

    # ─────────────────────────── TABLA ────────────────────────────────────

    def _update_datatable(self):
        self.data_table.clear()
        tmp = Cliente()
        tmp.set_connection(self.connection)
        self.data_table.insertMany(
            [
                (c.id, c.Nombre, c.Apellidos, c.CorreoElectronico, c.NumCelular)
                for c in tmp.select()
            ]
        )

    def _on_row_selected(self, values: tuple):
        """Llena el formulario derecho con los datos de la fila seleccionada."""
        if not values:
            return

        id_cliente, nombre, apellidos, correo, celular = values

        self.update_model.IdCliente = int(id_cliente)

        self.update_id.set(id_cliente)
        self.update_nombre.set(nombre)
        self.update_apellidos.set(apellidos)
        self.update_correo.set(correo)
        self.update_celular.set(celular)

    def _clear_add_form(self):
        """Limpia el formulario izquierdo tras una inserción."""
        self.add_nombre.clear()
        self.add_apellidos.clear()
        self.add_correo.clear()
        self.add_celular.clear()
        self.add_model = Cliente()
        self.add_model.set_connection(self.connection)

    def _clear_right_form(self):
        """Limpia el formulario derecho tras una eliminación."""
        self.update_id.set("")
        self.update_nombre.clear()
        self.update_apellidos.clear()
        self.update_correo.clear()
        self.update_celular.clear()

        self.update_model = Cliente()
        self.update_model.set_connection(self.connection)
