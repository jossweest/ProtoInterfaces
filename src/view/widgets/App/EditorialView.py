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


class EditorialView(ttk.Frame):
    def __init__(self, parent, connection: PostgresqlConnection):
        super().__init__(parent)
        self.connection = connection
