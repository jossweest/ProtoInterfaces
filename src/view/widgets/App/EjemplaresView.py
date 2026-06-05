import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.dialogs import Messagebox

from src.view.widgets.ComboField import ComboField
from src.view.widgets.DataTable import DataTable
from src.view.widgets.FormButton import FormButton, SaveButton
from src.view.widgets.LabeledEntry import LabeledEntry

from src.backend.PostgresqlConnection import PostgresqlConnection

from src.model.Libro import Libro
from src.model.Ejemplares import Ejemplares


class EjemplaresView(ttk.Frame):
    def __init__(self, parent, connection: PostgresqlConnection):
        super().__init__(parent)
        self.connection = connection

        self.add_model = Ejemplares()
        self.add_model.set_connection(connection)

        self.update_model = Ejemplares()
        self.update_model.set_connection(connection)

        self.build_ui()

    # ─────────────────────────── BUILD ────────────────────────────────────

    def build_ui(self):
        self.top_frame = ttk.Frame(self)
        self.top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self._load_keys()
        self._build_left_ui()
        self._build_right_ui()
        self._build_bottom_ui()
        self._update_datatable()

    def _build_left_ui(self):
        self.left = ttk.Labelframe(self.top_frame, text="Agregar datos")
        self.left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        ttk.Label(self.left, text="ISBN del libro").pack()
        self.add_libro = ComboField(
            self.left,
            values=self.libro_keys,
            onChange=lambda v: setattr(self.add_model.libro, "ISBN", v),
        )
        self.add_libro.pack()

        self.add_cantidad = LabeledEntry(
            self.left,
            label="Cantidad en existencia",
            onChange=lambda v: setattr(
                self.add_model, "cantidadExistencia", v),
        )
        self.add_cantidad.pack()

        self.add_precio = LabeledEntry(
            self.left,
            label="Precio de venta",
            onChange=lambda v: setattr(self.add_model, "precioVenta", v),
        )
        self.add_precio.pack()

        SaveButton(self.left, onClick=self._insert).pack(pady=8)

    def _build_right_ui(self):
        self.right = ttk.Labelframe(self.top_frame, text="Modificar datos")
        self.right.pack(side=tk.LEFT, fill=tk.BOTH,
                        expand=True, padx=5, pady=5)

        # ISBN: llave primaria, solo lectura
        self.update_isbn = LabeledEntry(self.right, label="ISBN")
        self.update_isbn.entry.configure(state="readonly")
        self.update_isbn.pack()

        # Campos editables
        self.update_cantidad = LabeledEntry(
            self.right, label="Cantidad en existencia")
        self.update_cantidad.pack()

        self.update_precio = LabeledEntry(self.right, label="Precio de venta")
        self.update_precio.pack()

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
            columns=["ISBN", "CantidadExistencia", "PrecioVenta"],
            height=7,
            onSelect=self._on_row_selected,
        )
        self.data_table.pack(fill=tk.BOTH, expand=True)

    # ─────────────────────────── VALIDACIÓN ───────────────────────────────

    def _validate_add(self) -> bool:
        if not self.add_libro.get():
            Messagebox.show_warning(
                "Selecciona un ISBN de libro.", title="Validación"
            )
            return False

        try:
            val = int(self.add_cantidad.get())
            if val < 0:
                raise ValueError
        except ValueError:
            Messagebox.show_warning(
                "La cantidad debe ser un número entero no negativo.", title="Validación"
            )
            return False

        try:
            val = float(self.add_precio.get())
            if val < 0:
                raise ValueError
        except ValueError:
            Messagebox.show_warning(
                "El precio debe ser un número válido y no negativo.", title="Validación"
            )
            return False

        return True

    def _validate_update(self) -> bool:
        if not self.update_isbn.get():
            Messagebox.show_warning(
                "Selecciona un registro de la tabla primero.", title="Validación"
            )
            return False

        try:
            val = int(self.update_cantidad.get())
            if val < 0:
                raise ValueError
        except ValueError:
            Messagebox.show_warning(
                "La cantidad debe ser un número entero no negativo.", title="Validación"
            )
            return False

        try:
            val = float(self.update_precio.get())
            if val < 0:
                raise ValueError
        except ValueError:
            Messagebox.show_warning(
                "El precio debe ser un número válido y no negativo.", title="Validación"
            )
            return False

        return True

    # ─────────────────────────── ACCIONES CRUD ────────────────────────────

    def _insert(self):
        if not self._validate_add():
            return
        try:
            self.add_model.cantidadExistencia = int(self.add_cantidad.get())
            self.add_model.precioVenta = float(self.add_precio.get())
            self.add_model.insert()
            self._update_datatable()
            self._clear_add_form()
            Messagebox.show_info(
                "Registro agregado correctamente.", title="Éxito")
        except Exception as e:
            Messagebox.show_error(f"Error al insertar:\n{e}", title="Error")

    def _update(self):
        if not self._validate_update():
            return
        try:
            self.update_model.cantidadExistencia = int(
                self.update_cantidad.get())
            self.update_model.precioVenta = float(self.update_precio.get())
            self.update_model.update()
            self._update_datatable()
            Messagebox.show_info(
                "Registro actualizado correctamente.", title="Éxito")
        except Exception as e:
            Messagebox.show_error(f"Error al actualizar:\n{e}", title="Error")

    def _delete(self):
        if not self.update_isbn.get():
            Messagebox.show_warning(
                "Selecciona un registro de la tabla primero.", title="Validación"
            )
            return

        confirm = Messagebox.yesno(
            f"¿Eliminar el ejemplar con ISBN {self.update_isbn.get()}?",
            title="Confirmar eliminación",
        )
        if not confirm in ["Yes", "Sí", "Ja"]:
            return

        try:
            self.update_model.delete()
            self._update_datatable()
            self._clear_right_form()
            Messagebox.show_info(
                "Registro eliminado correctamente.", title="Éxito")
        except Exception as e:
            Messagebox.show_error(f"Error al eliminar:\n{e}", title="Error")

    # ─────────────────────────── TABLA ────────────────────────────────────

    def _update_datatable(self):
        self.data_table.clear()
        tmp = Ejemplares()
        tmp.set_connection(self.connection)
        self.data_table.insertMany(
            [
                (item.libro.id, item.cantidadExistencia, item.precioVenta)
                for item in tmp.select()
            ]
        )

    def _on_row_selected(self, values: tuple):
        """Llena el formulario derecho con los datos de la fila seleccionada."""
        if not values:
            return

        isbn, cantidad, precio = values

        # Sincronizar update_model (PK)
        self.update_model.libro.id = isbn

        # Poblar campos del formulario derecho
        self.update_isbn.set(isbn)
        self.update_cantidad.set(cantidad)
        self.update_precio.set(precio)

    def _clear_add_form(self):
        """Limpia el formulario izquierdo después de una inserción exitosa."""
        self.add_libro.set("")
        self.add_cantidad.clear()
        self.add_precio.clear()
        # Reiniciar add_model
        self.add_model = Ejemplares()
        self.add_model.set_connection(self.connection)

    def _clear_right_form(self):
        """Limpia el formulario derecho tras una eliminación."""
        self.update_isbn.set("")
        self.update_cantidad.clear()
        self.update_precio.clear()

        # Reiniciar update_model
        self.update_model = Ejemplares()
        self.update_model.set_connection(self.connection)

    # ─────────────────────────── CLAVES FK ────────────────────────────────

    def _load_keys(self):
        tmp_libro = Libro()
        tmp_libro.set_connection(self.connection)
        self.libro_keys = [libro.id for libro in tmp_libro.select()]
