import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.dialogs import Messagebox
from src.view.widgets.App.Window import Window
from src.view.widgets.Sidebar import Sidebar


class App(Window):
    """Main class to contain the app"""

    def __init__(self):
        super().__init__()
        self.geometry("1000x600")

        self.sidebar = Sidebar()
        self.sidebar.configure(width=200)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)

        self.content = ttk.Frame(self)
        self.content.pack(expand=True, fill=tk.BOTH)
        self.sidebar.addButton("Libros", lambda: ttk.Frame())
        self.sidebar.addButton("Editoriales", lambda: ttk.Frame())
        self.sidebar.addButton("Autores", lambda: ttk.Frame())
        self.sidebar.addButton("Ejemplares", lambda: ttk.Frame())
        self.sidebar.addButton("Compras", lambda: ttk.Frame())
        self.sidebar.addButton("Clientes", lambda: ttk.Frame())

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
