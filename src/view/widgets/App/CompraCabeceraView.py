import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.dialogs import Messagebox

from src.view.widgets.ComboField import ComboField
from src.view.widgets.DataTable import DataTable
from src.view.widgets.FormButton import FormButton, SaveButton
from src.view.widgets.LabeledEntry import LabeledEntry

from src.backend.PostgresqlConnection import PostgresqlConnection

from src.model.Cliente import Cliente
from src.model.CompraCabecera import CompraCabecera


class CompraCabeceraView(ttk.Frame):
    def __init__(self, parent, connection: PostgresqlConnection):
        super().__init__(parent)
        self.connection = connection

        self.add_model = CompraCabecera()
        self.add_model.set_connection(connection)

        self.update_model = CompraCabecera()
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

        ttk.Label(self.left, text="Fecha (YYYY-MM-DD)").pack()
        self.add_fecha = LabeledEntry(
            self.left,
            label="",
            onChange=lambda v: setattr(self.add_model, "Fecha", v),
        )
        self.add_fecha.pack()

        ttk.Label(self.left, text="Cliente").pack()
        self.add_cliente = ComboField(
            self.left,
            values=self.cliente_keys,
            onChange=lambda v: setattr(
                self.add_model, "Cliente", Cliente(
                    IdCliente=int(v) if v else None)
            ),
        )
        self.add_cliente.pack()

        self.add_total = LabeledEntry(
            self.left,
            label="Total compra",
            onChange=lambda v: setattr(self.add_model, "TotalCompra", v),
        )
        self.add_total.pack()

        SaveButton(self.left, onClick=self._insert).pack(pady=8)

    def _build_right_ui(self):
        self.right = ttk.Labelframe(self.top_frame, text="Modificar datos")
        self.right.pack(side=tk.LEFT, fill=tk.BOTH,
                        expand=True, padx=5, pady=5)

        self.update_id = LabeledEntry(self.right, label="Id Compra")
        self.update_id.entry.configure(state="readonly")
        self.update_id.pack()

        self.update_fecha = LabeledEntry(
            self.right, label="Fecha (YYYY-MM-DD)")
        self.update_fecha.pack()

        ttk.Label(self.right, text="Cliente").pack()
        self.update_cliente = ComboField(
            self.right,
            values=self.cliente_keys,
            onChange=lambda v: setattr(
                self.update_model, "Cliente", Cliente(
                    IdCliente=int(v) if v else None)
            ),
        )
        self.update_cliente.pack()

        self.update_total = LabeledEntry(self.right, label="Total compra")
        self.update_total.pack()

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
            columns=["IdCompra", "Fecha", "IdCliente", "TotalCompra"],
            height=7,
            onSelect=self._on_row_selected,
        )
        self.data_table.pack(fill=tk.BOTH, expand=True)

    # ─────────────────────────── VALIDACIÓN ───────────────────────────────

    def _validate_add(self) -> bool:
        fecha = self.add_fecha.get()
        if not fecha:
            Messagebox.show_warning(
                "Ingresa la fecha de la compra.", title="Validación")
            return False

        # Validación simple de formato YYYY-MM-DD
        import re
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', fecha):
            Messagebox.show_warning(
                "La fecha debe tener el formato AAAA-MM-DD.", title="Validación"
            )
            return False

        if not self.add_cliente.get():
            Messagebox.show_warning(
                "Selecciona un cliente.", title="Validación")
            return False

        try:
            val = float(self.add_total.get())
            if val < 0:
                raise ValueError
        except ValueError:
            Messagebox.show_warning(
                "El total de la compra debe ser un número válido no negativo.",
                title="Validación"
            )
            return False

        return True

    def _validate_update(self) -> bool:
        if not self.update_id.get():
            Messagebox.show_warning(
                "Selecciona un registro de la tabla primero.", title="Validación"
            )
            return False

        fecha = self.update_fecha.get()
        if not fecha:
            Messagebox.show_warning(
                "Ingresa la fecha de la compra.", title="Validación")
            return False

        import re
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', fecha):
            Messagebox.show_warning(
                "La fecha debe tener el formato AAAA-MM-DD.", title="Validación"
            )
            return False

        if not self.update_cliente.get():
            Messagebox.show_warning(
                "Selecciona un cliente.", title="Validación")
            return False

        try:
            val = float(self.update_total.get())
            if val < 0:
                raise ValueError
        except ValueError:
            Messagebox.show_warning(
                "El total de la compra debe ser un número válido no negativo.",
                title="Validación"
            )
            return False

        return True

    # ─────────────────────────── ACCIONES CRUD ────────────────────────────

    def _insert(self):
        if not self._validate_add():
            return
        try:
            self.add_model.Fecha = self.add_fecha.get()
            self.add_model.TotalCompra = float(self.add_total.get())
            # El modelo ya tiene Cliente asignado desde el ComboField
            self.add_model.insert()
            self._update_datatable()
            self._clear_left_form()
            Messagebox.show_info(
                "Compra agregada correctamente.", title="Éxito")
        except Exception as e:
            Messagebox.show_error(f"Error al insertar:\n{e}", title="Error")

    def _update(self):
        if not self._validate_update():
            return
        try:
            self.update_model.Fecha = self.update_fecha.get()
            self.update_model.TotalCompra = float(self.update_total.get())
            # Cliente ya está actualizado mediante el onChange del ComboField
            self.update_model.update()
            self._update_datatable()
            Messagebox.show_info(
                "Compra actualizada correctamente.", title="Éxito")
        except Exception as e:
            Messagebox.show_error(f"Error al actualizar:\n{e}", title="Error")

    def _delete(self):
        if not self.update_id.get():
            Messagebox.show_warning(
                "Selecciona un registro de la tabla primero.", title="Validación"
            )
            return

        confirm = Messagebox.yesno(
            f"¿Eliminar la compra #{self.update_id.get()}?",
            title="Confirmar eliminación",
        )
        if confirm not in ["Yes", "Sí", "Ja"]:
            return

        try:
            self.update_model.delete()
            self._update_datatable()
            self._clear_right_form()
            Messagebox.show_info(
                "Compra eliminada correctamente.", title="Éxito")
        except Exception as e:
            Messagebox.show_error(f"Error al eliminar:\n{e}", title="Error")

    # ─────────────────────────── TABLA ────────────────────────────────────

    def _update_datatable(self):
        self.data_table.clear()
        tmp = CompraCabecera()
        tmp.set_connection(self.connection)
        self.data_table.insertMany(
            [
                (item.IdCompra, item.Fecha, item.Cliente.id, item.TotalCompra)
                for item in tmp.select()
            ]
        )

    def _on_row_selected(self, values: tuple):
        """Llena el formulario derecho con los datos de la fila seleccionada."""
        if not values:
            return

        id_compra, fecha, id_cliente, total = values

        # Sincronizar update_model
        self.update_model.IdCompra = int(id_compra)
        self.update_model.Fecha = fecha
        self.update_model.Cliente = Cliente(IdCliente=int(id_cliente))
        self.update_model.TotalCompra = float(total)

        # Poblar campos del formulario derecho
        self.update_id.set(id_compra)
        self.update_fecha.set(fecha)
        self.update_cliente.set(id_cliente)
        self.update_total.set(total)

    def _clear_left_form(self):
        """Limpia el formulario izquierdo después de una inserción."""
        self.add_fecha.clear()
        self.add_cliente.set("")
        self.add_total.clear()
        # Reiniciar modelo
        self.add_model = CompraCabecera()
        self.add_model.set_connection(self.connection)

    def _clear_right_form(self):
        """Limpia el formulario derecho tras una eliminación."""
        self.update_id.set("")
        self.update_fecha.clear()
        self.update_cliente.set("")
        self.update_total.clear()

        # Reiniciar update_model
        self.update_model = CompraCabecera()
        self.update_model.set_connection(self.connection)

    # ─────────────────────────── CLAVES FORÁNEAS ──────────────────────────

    def _load_keys(self):
        tmp_cliente = Cliente()
        tmp_cliente.set_connection(self.connection)
        self.cliente_keys = [cliente.id for cliente in tmp_cliente.select()]
