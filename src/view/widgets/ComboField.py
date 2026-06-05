import tkinter as tk
from tkinter import ttk
from typing import Callable, List, Optional


class ComboField(ttk.Combobox):

    DEFAULT_WIDTH = 32

    def __init__(
        self,
        parent: tk.Widget,
        values: List[str] = None,
        width: int = DEFAULT_WIDTH,
        onChange: Optional[Callable[[str], None]] = None,
        **kwargs,
    ):
        super().__init__(parent, width=width, **kwargs)

        if values:
            self.config(values=values)

        if onChange:
            self.bind("<<ComboboxSelected>>", lambda _: onChange(self.get()))

    def clear(self):
        """Limpia la selección actual sin borrar las opciones."""
        self.set("")

    def setValues(self, values: List[str]):
        """Reemplaza la lista de opciones del combobox."""
        self.config(values=values)


if __name__ == "__main__":
    from src.view.widgets.App.Window import Window
    window = Window()

    window.title("ComboField")

    lbl = tk.Label(window, text="Elige un autor:")
    lbl.pack(padx=20, pady=(15, 0))

    resultado = tk.Label(window, text="Selección: (ninguna)")
    resultado.pack(pady=4)

    combo = ComboField(
        window,
        values=["Edgar Allan Poe", "Osamu Dazai",
                "Franz Kafka", "Mary Shelley"],
        onChange=lambda v: resultado.config(text=f"Selección: {v}"),
    )
    combo.pack(padx=20, pady=8)

    tk.Button(window, text="Limpiar", command=combo.clear).pack(pady=8)
    window.mainloop()
