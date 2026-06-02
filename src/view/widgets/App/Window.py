
import tkinter as tk
import ttkbootstrap as ttk


class Window(ttk.Window):
    def __init__(
            self,
            title=f"Librería pollitos",
            themename="yeti",
            iconphoto=None,
            size=[800, 496],
            position=None,
            minsize=None,
            maxsize=None,
            resizable=None,
            hdpi=True,
            scaling=None,
            transient=None,
            overrideredirect=False,
            alpha=1
    ):

        super().__init__(
            title,
            themename,
            iconphoto,
            size,
            position,
            minsize,
            maxsize,
            resizable,
            hdpi,
            scaling,
            transient,
            overrideredirect,
            alpha
        )


if __name__ == "__main__":
    view = Window()
    view.mainloop()
