import tkinter as tk
import ttkbootstrap as ttk
from typing import Callable, List, Optional


class FormButton(ttk.Button):

    def __init__(
        self,
        parent: tk.Widget,
        text: str,
        onClick: Optional[Callable[[], None]] = None,
        **kwargs,
    ):
        super().__init__(parent, text=text, command=onClick, **kwargs)


class SaveButton(FormButton):

    def __init__(
        self,
        parent: tk.Widget,
        text: str = "Guardar",
        onClick: Optional[Callable[[], None]] = None,
        **kwargs,
    ):
        super().__init__(parent, text=text, onClick=onClick, **kwargs)


class ClearButton(FormButton):
    def __init__(
        self,
        parent: tk.Widget,
        fields: Optional[List] = None,
        onClick: Optional[Callable[[], None]] = None,
        **kwargs,
    ):
        if fields is not None:
            def onClick(): return [f.clear() for f in fields]

        super().__init__(parent, text="Limpiar", onClick=onClick, **kwargs)


if __name__ == "__main__":
    from src.view.widgets.App.Window import Window
    from src.view.widgets.EntryField import EntryField

    window = Window()
    window.title("FormButton")

    log = tk.Label(window, text="(esperando acción…)")
    log.pack(padx=20, pady=15)

    SaveButton(
        window,
        text="Guardar libro",
        onClick=lambda: log.config(text="✔ Libro guardado"),
    ).pack(padx=20, pady=5)

    FormButton(
        window,
        text="Buscar por ISBN",
        onClick=lambda: log.config(text="🔍 Buscando…"),
    ).pack(padx=20, pady=5)

    entry = EntryField(window)
    entry.pack(padx=20, pady=5)

    ClearButton(window, fields=[entry]).pack(padx=20, pady=5)

    window.mainloop()
