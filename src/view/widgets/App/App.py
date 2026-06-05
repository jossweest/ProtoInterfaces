import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.dialogs import Messagebox
from src.view.widgets.App.Window import Window
from src.view.widgets.Sidebar import Sidebar

from src.utils.config import config

from src.backend.PostgresqlConnection import PostgresqlConnection

from src.view.widgets.App.AutorView import AutorView
from src.view.widgets.App.ClienteView import ClienteView
from src.view.widgets.App.CompraCabeceraView import CompraCabeceraView
from src.view.widgets.App.CompraDetalleView import CompraDetalleView
from src.view.widgets.App.EditorialView import EditorialView
from src.view.widgets.App.EjemplaresView import EjemplaresView
from src.view.widgets.App.LibroView import LibroView


class App(Window):
    """Main class to contain the app"""

    def __init__(self):
        super().__init__()

        self.psql_connection = PostgresqlConnection()
        self.psql_connection.connect(**config())

        self.geometry("1000x600")

        self.sidebar = Sidebar()
        self.sidebar.configure(width=200)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)

        self.content = ttk.Frame(self)
        self.content.pack(expand=True, fill=tk.BOTH)
        self.sidebar.addButton(
            "Autores", lambda: AutorView(self.content, self.psql_connection))
        self.sidebar.addButton(
            "Clientes", lambda: ClienteView(self.content, self.psql_connection))
        self.sidebar.addButton(
            "Cabeceras de compras", lambda: CompraCabeceraView(self.content, self.psql_connection))
        self.sidebar.addButton(
            "Detalles de compras", lambda: CompraDetalleView(self.content, self.psql_connection))
        self.sidebar.addButton(
            "Editoriales", lambda: EditorialView(self.content, self.psql_connection))
        self.sidebar.addButton(
            "Ejemplares", lambda: EjemplaresView(self.content, self.psql_connection))
        self.sidebar.addButton(
            "Libros", lambda: LibroView(self.content, self.psql_connection))

        self.sidebar.selectWidget("Libros")

    def destroy(self):
        return super().destroy()

    def mainloop(self, n=0):

        try:
            super().mainloop(n)
        except Exception as e:
            Messagebox.show_error(
                title="Error", message=f"Error en la aplicación : {e}"
            )


if __name__ == "__main__":

    app = App()
    app.mainloop()
