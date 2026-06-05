import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.dialogs import Messagebox
from tkinter import ttk as tkttk

from src.view.widgets.DataTable import DataTable
from src.view.widgets.LabeledEntry import LabeledEntry
from src.view.widgets.FormButton import FormButton

from src.backend.PostgresqlConnection import PostgresqlConnection


class ReportesView(ttk.Frame):
    def __init__(self, parent, connection: PostgresqlConnection):
        super().__init__(parent)
        self.connection = connection
        self.build_ui()

    def build_ui(self):
        # Usamos un Notebook para organizar los tres reportes en pestañas
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Pestaña 1: Libros en pedidos de una fecha
        self.tab_fecha = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_fecha, text="Libros por fecha de pedido")
        self._build_reporte_fecha()

        # Pestaña 2: Libros con stock < 5
        self.tab_stock = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_stock, text="Stock bajo (menor a 5)")
        self._build_reporte_stock()

        # Pestaña 3: Todos los libros con autor y editorial
        self.tab_completo = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_completo,
                          text="Libros con autor y editorial")
        self._build_reporte_completo()

    # ─────────────────────────── REPORTE 1 ────────────────────────────────

    def _build_reporte_fecha(self):
        # Marco superior para controles
        frame_controles = ttk.LabelFrame(self.tab_fecha, text="Parámetros")
        frame_controles.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        # Campo de fecha
        self.fecha_entry = LabeledEntry(
            frame_controles,
            label="Fecha del pedido (YYYY-MM-DD):",
            width=30
        )
        self.fecha_entry.pack(side=tk.LEFT, padx=5, pady=5)

        # Botón generar
        self.btn_generar_fecha = FormButton(
            frame_controles,
            text="Generar reporte",
            onClick=self._generar_reporte_fecha,
            bootstyle="primary"
        )
        self.btn_generar_fecha.pack(side=tk.LEFT, padx=5, pady=5)

        # Tabla para resultados
        self.tabla_fecha = DataTable(
            self.tab_fecha,
            columns=["ISBN", "Título", "Cantidad", "Precio", "Fecha pedido"],
            height=15
        )
        self.tabla_fecha.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def _generar_reporte_fecha(self):
        """Lógica para reporte 1 (pendiente de implementar)"""
        fecha = self.fecha_entry.get()
        if not fecha:
            Messagebox.show_warning(
                "Por favor ingrese una fecha.", title="Validación")
            return
        # TODO: Implementar la consulta real
        # Por ahora, solo mostrar un mensaje
        Messagebox.show_info(
            "Funcionalidad no implementada aún.\n"
            f"Consultaría libros en pedidos con fecha: {fecha}",
            title="Reporte"
        )
        # Limpiar tabla (opcional)
        self.tabla_fecha.clear()
        # Aquí se llenaría la tabla con los resultados

    # ─────────────────────────── REPORTE 2 ────────────────────────────────

    def _build_reporte_stock(self):
        # Marco de controles (aunque este reporte no necesita parámetros)
        frame_controles = ttk.LabelFrame(self.tab_stock, text="Parámetros")
        frame_controles.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        ttk.Label(frame_controles, text="Muestra libros con cantidad en stock < 5").pack(
            side=tk.LEFT, padx=5)

        self.btn_generar_stock = FormButton(
            frame_controles,
            text="Generar reporte",
            onClick=self._generar_reporte_stock,
            bootstyle="primary"
        )
        self.btn_generar_stock.pack(side=tk.LEFT, padx=5, pady=5)

        # Tabla para resultados
        self.tabla_stock = DataTable(
            self.tab_stock,
            columns=["ISBN", "Título", "Stock", "Ubicación"],
            height=15
        )
        self.tabla_stock.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def _generar_reporte_stock(self):
        """Lógica para reporte 2 (pendiente de implementar)"""
        # TODO: Implementar consulta de libros con stock < 5
        Messagebox.show_info(
            "Funcionalidad no implementada aún.\n"
            "Consultaría libros con cantidad en stock menor a 5.",
            title="Reporte"
        )
        self.tabla_stock.clear()

    # ─────────────────────────── REPORTE 3 ────────────────────────────────

    def _build_reporte_completo(self):
        # Marco de controles (sin parámetros)
        frame_controles = ttk.LabelFrame(self.tab_completo, text="Parámetros")
        frame_controles.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        ttk.Label(frame_controles, text="Todos los libros con nombre de autor y editorial").pack(
            side=tk.LEFT, padx=5)

        self.btn_generar_completo = FormButton(
            frame_controles,
            text="Generar reporte",
            onClick=self._generar_reporte_completo,
            bootstyle="primary"
        )
        self.btn_generar_completo.pack(side=tk.LEFT, padx=5, pady=5)

        # Tabla para resultados
        self.tabla_completo = DataTable(
            self.tab_completo,
            columns=["ISBN", "Título", "Autor", "Editorial", "Ubicación"],
            height=15
        )
        self.tabla_completo.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def _generar_reporte_completo(self):
        """Lógica para reporte 3 (pendiente de implementar)"""
        # TODO: Consultar todos los libros con nombre de autor y editorial
        Messagebox.show_info(
            "Funcionalidad no implementada aún.\n"
            "Consultaría todos los libros con autor y editorial.",
            title="Reporte"
        )
        self.tabla_completo.clear()
