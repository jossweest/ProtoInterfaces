import tkinter as tk
import ttkbootstrap as ttk
from typing import Dict, Callable, Union
from dataclasses import dataclass
from ttkbootstrap import constants as c


@dataclass
class currentWidget:
    name: str
    widget: tk.Widget


class Sidebar(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master, style=c.DARK)

        self.configure(
            width=400,
            padding=[20, 30],

        )

        self.buttonData: Dict[str, Dict[str, Union[Callable, ttk.Button]]] = {}

        self.currentWidget: currentWidget = currentWidget(None, None)

    def onClick(self, name: str):

        if self.currentWidget.name == name:
            return
        if not self.currentWidget.widget is None:
            self.currentWidget.widget.destroy()

        newWidget = self.buttonData.get(name).get("widget", None)()
        self.currentWidget = currentWidget(name, newWidget)

        self.currentWidget.widget.pack(fill=tk.BOTH, expand=True)

    def addButton(self, name: str, widget: Callable, onClick=None):

        if onClick is None:
            def onClick(): return self.onClick(name)

        button = ttk.Button(
            self,
            text=name,
            command=lambda: onClick(),
            padding=[3, 10],
            style=c.DARK
        )
        button.pack(fill=tk.X, expand=True)

        self.buttonData[name] = {"widget": widget, "button": button}

    def selectWidget(self, name):
        self.onClick(name)


if __name__ == "__main__":
    from src.view.widgets.App.Window import Window
    app = Window()

    sidebar = Sidebar(app)
    sidebar.pack(side=tk.LEFT, fill=tk.Y)
    i = 0

    def primary(): return ttk.Frame(app, bootstyle="primary")
    def secondary(): return ttk.Frame(app, bootstyle="secondary")
    def warning(): return ttk.Frame(app, bootstyle="warning")

    sidebar.addButton("primary", primary)
    sidebar.addButton("secondary", secondary)
    sidebar.addButton("warning", warning)

    app.mainloop()
