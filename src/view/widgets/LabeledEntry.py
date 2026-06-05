import tkinter as tk
import ttkbootstrap as ttk
from typing import Callable, Optional
from src.model.Libro import Libro


class LabeledEntry(ttk.Frame):

    DEFAULT_ENTRY_WIDTH = 35
    DEFAULT_LABEL_WIDTH = 18

    def __init__(
        self,
        parent: tk.Widget,
        label: str,
        width: int = DEFAULT_ENTRY_WIDTH,
        label_width: int = DEFAULT_LABEL_WIDTH,
        onChange: Optional[Callable[[str], None]] = None,
        **kwargs,
    ):
        super().__init__(parent, **kwargs)

        self._label = ttk.Label(
            self, text=label, width=label_width, anchor="w")
        self._label.grid(row=0, column=0, padx=(10, 5), pady=8, sticky="w")

        self._var = tk.StringVar()
        self._entry = ttk.Entry(self, width=width, textvariable=self._var)
        self._entry.grid(row=0, column=1, padx=(5, 10), pady=8)

        if onChange:
            self._var.trace_add("write", lambda *_: onChange(self._var.get()))

    def get(self) -> str:
        """Devuelve el valor actual del Entry."""
        return self._var.get()

    def set(self, value: str):
        """Reemplaza el contenido del Entry (dispara onChange)."""
        self._var.set(str(value))

    def clear(self):
        """Vacía el Entry (dispara onChange)."""
        self._var.set("")

    @property
    def entry(self) -> ttk.Entry:
        """Referencia directa al widget Entry interno."""
        return self._entry

    @property
    def label(self) -> ttk.Label:
        """Referencia directa al widget Label interno."""
        return self._label


if __name__ == "__main__":
    from src.view.widgets.App.Window import Window

    window = Window()
    model = Libro()

    frame = ttk.LabelFrame(window, text="Registro de libro")
    frame.pack(padx=20, pady=20)

    LabeledEntry(
        frame,
        label="ISBN",
        onChange=lambda v: setattr(model, "ISBN", v),
    ).grid(row=0, column=0, columnspan=2, sticky="w")

    LabeledEntry(
        frame,
        label="Título",
        onChange=lambda v: setattr(model, "titulo", v),
    ).grid(row=1, column=0, columnspan=2, sticky="w")

    tk.Button(
        window,
        text="Ver modelo",
        command=lambda: print(
            f"ISBN={model.ISBN!r}  titulo={model.Titulo!r}"),
    ).pack(pady=10)

    window.mainloop()
