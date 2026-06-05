import tkinter as tk
import ttkbootstrap as ttk
from typing import Callable, List, Optional, Tuple


class DataTable(ttk.Frame):

    DEFAULT_COL_WIDTH = 120

    def __init__(
        self,
        parent: tk.Widget,
        columns: List[str],
        height: int = 5,
        col_width: int = DEFAULT_COL_WIDTH,
        onSelect: Optional[Callable[[Tuple], None]] = None,
        **kwargs,
    ):
        super().__init__(parent, **kwargs)

        self._columns = columns
        self._col_width = col_width
        self._onSelect = onSelect
        self._build(height)

    def _build(self, height: int):
        scrollbar = ttk.Scrollbar(self, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        self._tree = ttk.Treeview(
            self,
            columns=self._columns,
            show="headings",
            height=height,
            yscrollcommand=scrollbar.set,
        )
        scrollbar.config(command=self._tree.yview)

        for col in self._columns:
            self._tree.heading(col, text=col)
            self._tree.column(col, width=self._col_width, anchor="w")

        self._tree.pack(fill="both", expand=True)

        if self._onSelect:
            self._tree.bind(
                "<<TreeviewSelect>>",
                lambda _: self._onSelect(self.getSelected()),
            )

    def insert(self, values: Tuple):
        """Agrega una fila al final de la tabla."""
        self._tree.insert("", "end", values=values)

    def insertMany(self, rows: List[Tuple]):
        """Agrega varias filas de una vez."""
        for row in rows:
            self.insert(row)

    def clear(self):
        """Elimina todas las filas de la tabla."""
        for item in self._tree.get_children():
            self._tree.delete(item)

    def getSelected(self) -> Optional[Tuple]:
        """
        Devuelve los valores de la fila actualmente seleccionada.
        Retorna None si no hay selección.
        """
        selected = self._tree.focus()
        return self._tree.item(selected, "values") if selected else None

    def setColumnWidth(self, col: str, width: int):
        """Ajusta el ancho de una columna específica en píxeles."""
        self._tree.column(col, width=width)

    @property
    def tree(self) -> ttk.Treeview:
        """Referencia directa al widget Treeview interno."""
        return self._tree


if __name__ == "__main__":
    from src.view.widgets.App.Window import Window
    window = Window()

    info = tk.Label(window, text="Haz clic en una fila")
    info.pack(pady=10)

    tabla = DataTable(
        window,
        columns=["ISBN", "Título", "Autor", "Stock"],
        height=5,
        onSelect=lambda row: info.config(
            text=f"Seleccionado: {row[1]}  (ISBN: {row[0]})" if row else "—"
        ),
    )
    tabla.pack(fill="both", expand=True, padx=20, pady=10)

    tabla.insertMany([
        ("978-0141439815", "El cuervo",             "Edgar Allan Poe", 4),
        ("978-0811204811", "Indigno de ser humano",  "Osamu Dazai",    8),
        ("978-0805209990", "La metamorfosis",        "Franz Kafka",    3),
    ])

    window.mainloop()
