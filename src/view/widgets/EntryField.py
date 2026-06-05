import tkinter as tk
from tkinter import ttk
from typing import Callable, Optional


class EntryField(ttk.Entry):

    DEFAULT_WIDTH = 35

    def __init__(
        self,
        parent: tk.Widget,
        width: int = DEFAULT_WIDTH,
        onChange: Optional[Callable[[str], None]] = None,
        **kwargs,
    ):
        self._var = tk.StringVar()
        super().__init__(parent, width=width, textvariable=self._var, **kwargs)

        if onChange:
            self._var.trace_add("write", lambda *_: onChange(self._var.get()))

    # ------------------------------------------------------------------
    # API pública
    # ------------------------------------------------------------------

    def get(self) -> str:
        return self._var.get()

    def set(self, value: str):
        """Reemplaza el contenido (también dispara onChange si está definido)."""
        self._var.set(str(value))

    def clear(self):
        """Vacía el campo (también dispara onChange si está definido)."""
        self._var.set("")


# ---------------------------------------------------------------------------
# Prueba rápida
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    root.title("EntryField – prueba")

    lbl = tk.Label(root, text="Escribe algo:")
    lbl.pack(padx=20, pady=(15, 0))

    field = EntryField(
        root,
        width=30,
        onChange=lambda v: resultado.config(text=f"Valor actual: '{v}'"),
    )
    field.pack(padx=20, pady=8)
    field.set("Valor inicial")

    resultado = tk.Label(root, text="Valor actual: 'Valor inicial'")
    resultado.pack(pady=4)

    tk.Button(root, text="Limpiar", command=field.clear).pack(pady=8)
    root.mainloop()
