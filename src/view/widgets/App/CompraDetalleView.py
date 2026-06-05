import ttkbootstrap as ttk
import tkinter as tk

from src.view.widgets.ComboField import ComboField
from src.view.widgets.DataTable import DataTable
from src.view.widgets.FormButton import FormButton, ClearButton, SaveButton
from src.view.widgets.LabeledEntry import LabeledEntry

from typing import Optional, List, Tuple

from src.backend.PostgresqlConnection import PostgresqlConnection

from src.model.Autor import Autor
from src.model.Cliente import Cliente
from src.model.CompraCabecera import CompraCabecera
from src.model.CompraDetalle import CompraDetalle
from src.model.Editorial import Editorial
from src.model.Ejemplares import Ejemplares
from src.model.Libro import Libro


class CompraDetalleView(ttk.Frame):
    def __init__(self, parent, connection: PostgresqlConnection):
        super().__init__(parent)
        self.connection = connection

        self.add_model = CompraDetalle()
        self.add_model.set_connection(connection)

        self.update_model = CompraDetalle()
        self.update_model.set_connection(connection)

        self.current_selection = None

        self.build_ui()

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

        ttk.Label(self.left, text="Id de compra cabecera").pack()
        self.add_compra_cabecera = ComboField(
            self.left, values=self.compra_cabecera_keys,
            onChange=lambda v: setattr(
                self.add_model.compraCabecera, "IdCompra", v)
        )
        self.add_compra_cabecera.pack()
        ttk.Label(self.left, text="ISBN del libro").pack()
        self.add_libro = ComboField(
            self.left, values=self.libro_keys,
            onChange=lambda v: setattr(
                self.add_model.libro, "ISBN", v)
        )
        self.add_libro.pack()
        self.add_cantidad = LabeledEntry(
            self.left, label="Cantidad", onChange=lambda v: setattr(self.add_model, "Cantidad", v)
        )
        self.add_cantidad.pack()
        self.add_precio = LabeledEntry(self.left, label="Precio")
        self.add_precio.pack()

        save_button = SaveButton(self.left, onClick=self._insert)
        save_button.pack()

    def _build_right_ui(self):
        self.right = ttk.Labelframe(self.top_frame, text="Modificar datos")
        self.right.pack(side=tk.LEFT, fill=tk.BOTH,
                        expand=True, padx=5, pady=5)

    def _build_bottom_ui(self):
        self.bottom = ttk.Labelframe(self, text="Consultar datos")
        self.bottom.pack(
            side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5
        )

        self.data_table = DataTable(
            self.bottom,
            columns=["IdCompra", "ISBN", "Cantidad", "Precio"],
            height=7,
            onSelect=self._on_row_selected
        )

        self.data_table.pack(fill=tk.BOTH, expand=True)

    def _insert(self):

        print(f"{self.add_model.compraCabecera.id}")
        self.add_model.insert()
        self._update_datatable()

    def _update_datatable(self):

        self.data_table.clear()

        tmp_model = CompraDetalle()
        tmp_model.set_connection(self.connection)
        self.data = tmp_model.select()

        self.data_table.insertMany(
            [
                (item.compraCabecera.id, item.libro.id, item.Cantidad, item.Precio) for item in self.data
            ]
        )

    def _on_row_selected(self, values: tuple):
        if not values:
            return

        self.update_model.compraCabecera.id = int(values[0])
        self.update_model.libro.id = values[1]
        self.update_model.Cantidad = int(values[2])
        self.update_model.Precio = float(values[3])

    def _load_keys(self):

        tmp_libro = Libro()
        tmp_libro.set_connection(self.connection)
        tmp_compra_cabecera = CompraCabecera()
        tmp_compra_cabecera.set_connection(self.connection)

        self.libro_keys = [libro.id for libro in tmp_libro.select()]
        self.compra_cabecera_keys = [
            compra_cabecera.id for compra_cabecera in tmp_compra_cabecera.select()
        ]
