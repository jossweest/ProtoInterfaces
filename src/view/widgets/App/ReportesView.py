import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.dialogs import Messagebox
from datetime import datetime
import re

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
        frame_controles = ttk.LabelFrame(self.tab_fecha, text="Parámetros")
        frame_controles.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        self.fecha_entry = LabeledEntry(
            frame_controles,
            label="Fecha del pedido (YYYY-MM-DD):",
            width=30
        )
        self.fecha_entry.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_generar_fecha = FormButton(
            frame_controles,
            text="Generar reporte",
            onClick=self._generar_reporte_fecha,
            bootstyle="primary"
        )
        self.btn_generar_fecha.pack(side=tk.LEFT, padx=5, pady=5)

        self.tabla_fecha = DataTable(
            self.tab_fecha,
            columns=["ISBN", "Título", "Cantidad", "Precio", "Fecha pedido"],
            height=15
        )
        self.tabla_fecha.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def _generar_reporte_fecha(self):
        fecha = self.fecha_entry.get().strip()
        if not fecha:
            Messagebox.show_warning(
                "Ingrese una fecha en formato YYYY-MM-DD", title="Validación")
            return

        if not re.match(r'^\d{4}-\d{2}-\d{2}$', fecha):
            Messagebox.show_warning(
                "Formato de fecha inválido. Use YYYY-MM-DD", title="Validación")
            return

        try:
            datetime.strptime(fecha, '%Y-%m-%d')
        except ValueError:
            Messagebox.show_warning(
                "Fecha no válida (ejemplo: 2025-03-20)", title="Validación")
            return

        # Construir consulta con la fecha interpolada (ya validada)
        query = f"""
            SELECT 
                l.isbn, 
                l.titulo, 
                cd.cantidad, 
                cd.precio, 
                cc.fecha
            FROM compradetalle cd
            JOIN compracabecera cc ON cd.idcompra = cc.idcompra
            JOIN libro l ON cd.isbn = l.isbn
            WHERE cc.fecha = '{fecha}'
            ORDER BY cc.fecha, l.titulo;
        """

        try:
            resultados = self.connection._execute_and_fetch_all(query)
            self.tabla_fecha.clear()
            if resultados:
                self.tabla_fecha.insertMany(resultados)
                Messagebox.show_info(
                    f"Se encontraron {len(resultados)} registros.", title="Reporte")
            else:
                Messagebox.show_info(
                    "No hay libros en pedidos para la fecha especificada.", title="Reporte")
        except Exception as e:
            Messagebox.show_error(f"Error al consultar: {e}", title="Error")

    # ─────────────────────────── REPORTE 2 ────────────────────────────────

    def _build_reporte_stock(self):
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

        self.tabla_stock = DataTable(
            self.tab_stock,
            columns=["ISBN", "Título", "Stock", "Ubicación"],
            height=15
        )
        self.tabla_stock.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def _generar_reporte_stock(self):
        query = """
            SELECT 
                l.isbn, 
                l.titulo, 
                e.cantidadexistencia AS stock, 
                l.ubicacion
            FROM libro l
            JOIN ejemplares e ON l.isbn = e.isbn
            WHERE e.cantidadexistencia < 5
            ORDER BY e.cantidadexistencia;
        """

        try:
            resultados = self.connection._execute_and_fetch_all(query)
            self.tabla_stock.clear()
            if resultados:
                self.tabla_stock.insertMany(resultados)
                Messagebox.show_info(
                    f"Se encontraron {len(resultados)} libros con stock bajo.", title="Reporte")
            else:
                Messagebox.show_info(
                    "No hay libros con stock menor a 5.", title="Reporte")
        except Exception as e:
            Messagebox.show_error(f"Error al consultar: {e}", title="Error")

    # ─────────────────────────── REPORTE 3 ────────────────────────────────

    def _build_reporte_completo(self):
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

        self.tabla_completo = DataTable(
            self.tab_completo,
            columns=["ISBN", "Título", "Autor", "Editorial", "Ubicación"],
            height=15
        )
        self.tabla_completo.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def _generar_reporte_completo(self):
        query = """
            SELECT 
                l.isbn, 
                l.titulo, 
                a.nombre AS autor, 
                e.nombre AS editorial, 
                l.ubicacion
            FROM libro l
            JOIN autores a ON l.idautor = a.idautor
            JOIN editoriales e ON l.ideditorial = e.ideditorial
            ORDER BY l.titulo;
        """

        try:
            resultados = self.connection._execute_and_fetch_all(query)
            self.tabla_completo.clear()
            if resultados:
                self.tabla_completo.insertMany(resultados)
                Messagebox.show_info(
                    f"Se encontraron {len(resultados)} libros registrados.", title="Reporte")
            else:
                Messagebox.show_info(
                    "No hay libros en la base de datos.", title="Reporte")
        except Exception as e:
            Messagebox.show_error(f"Error al consultar: {e}", title="Error")
