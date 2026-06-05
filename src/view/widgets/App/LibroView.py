import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.dialogs import Messagebox

from src.view.widgets.ComboField import ComboField
from src.view.widgets.DataTable import DataTable
from src.view.widgets.FormButton import FormButton, SaveButton
from src.view.widgets.LabeledEntry import LabeledEntry

from src.backend.PostgresqlConnection import PostgresqlConnection

from src.model.Libro import Libro
from src.model.Editorial import Editorial
from src.model.Autor import Autor


class LibroView(ttk.Frame):
    def __init__(self, parent, connection: PostgresqlConnection):
        super().__init__(parent)
        self.connection = connection

        self.add_model = Libro()
        self.add_model.set_connection(connection)

        self.update_model = Libro()
        self.update_model.set_connection(connection)

        self.build_ui()

    # ─────────────────────────── BUILD ────────────────────────────────────

    def build_ui(self):
        self.top_frame = ttk.Frame(self)
        self.top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self._load_keys()
        self._build_left_ui()
        self._build_right_ui()
        self._build_bottom_ui()
        self._update_datatable()

    def _build_left_ui(self):
        self.left = ttk.Labelframe(self.top_frame, text="Agregar datos")
        self.left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        # ISBN (clave primaria)
        self.add_isbn = LabeledEntry(
            self.left,
            label="ISBN",
            onChange=lambda v: setattr(self.add_model, "ISBN", v),
        )
        self.add_isbn.pack()

        # Título
        self.add_titulo = LabeledEntry(
            self.left,
            label="Título",
            onChange=lambda v: setattr(self.add_model, "Titulo", v),
        )
        self.add_titulo.pack()

        # Editorial (FK)
        ttk.Label(self.left, text="Editorial").pack()
        self.add_editorial = ComboField(
            self.left,
            values=self.editorial_keys,
            onChange=lambda v: setattr(
                self.add_model.Editorial, "id", int(v) if v else None
            ),
        )
        self.add_editorial.pack()

        # Autor (FK)
        ttk.Label(self.left, text="Autor").pack()
        self.add_autor = ComboField(
            self.left,
            values=self.autor_keys,
            onChange=lambda v: setattr(
                self.add_model.Autor, "id", int(v) if v else None
            ),
        )
        self.add_autor.pack()

        # Ubicación
        self.add_ubicacion = LabeledEntry(
            self.left,
            label="Ubicación",
            onChange=lambda v: setattr(self.add_model, "Ubicación", v),
        )
        self.add_ubicacion.pack()

        SaveButton(self.left, onClick=self._insert).pack(pady=8)

    def _build_right_ui(self):
        self.right = ttk.Labelframe(self.top_frame, text="Modificar datos")
        self.right.pack(side=tk.LEFT, fill=tk.BOTH,
                        expand=True, padx=5, pady=5)

        # ISBN (PK) – solo lectura
        self.update_isbn = LabeledEntry(self.right, label="ISBN")
        self.update_isbn.entry.configure(state="readonly")
        self.update_isbn.pack()

        # Campos editables
        self.update_titulo = LabeledEntry(self.right, label="Título")
        self.update_titulo.pack()

        ttk.Label(self.right, text="Editorial").pack()
        self.update_editorial = ComboField(
            self.right,
            values=self.editorial_keys,
            onChange=lambda v: setattr(
                self.update_model.Editorial, "id", int(v) if v else None
            ),
        )
        self.update_editorial.pack()

        ttk.Label(self.right, text="Autor").pack()
        self.update_autor = ComboField(
            self.right,
            values=self.autor_keys,
            onChange=lambda v: setattr(
                self.update_model.Autor, "id", int(v) if v else None
            ),
        )
        self.update_autor.pack()

        self.update_ubicacion = LabeledEntry(self.right, label="Ubicación")
        self.update_ubicacion.pack()

        btn_frame = ttk.Frame(self.right)
        btn_frame.pack(pady=8)

        SaveButton(btn_frame, onClick=self._update).pack(side=tk.LEFT, padx=4)
        FormButton(
            btn_frame,
            text="Eliminar",
            onClick=self._delete,
            bootstyle="danger",
        ).pack(side=tk.LEFT, padx=4)

    def _build_bottom_ui(self):
        self.bottom = ttk.Labelframe(self, text="Consultar datos")
        self.bottom.pack(side=tk.TOP, fill=tk.BOTH,
                         expand=True, padx=5, pady=5)

        self.data_table = DataTable(
            self.bottom,
            columns=["ISBN", "Título", "IdEditorial", "IdAutor", "Ubicación"],
            height=7,
            onSelect=self._on_row_selected,
        )
        self.data_table.pack(fill=tk.BOTH, expand=True)

    # ─────────────────────────── VALIDACIÓN ───────────────────────────────

    def _validate_add(self) -> bool:
        if not self.add_isbn.get():
            Messagebox.show_warning(
                "El ISBN es obligatorio.", title="Validación")
            return False

        if not self.add_titulo.get():
            Messagebox.show_warning(
                "El título es obligatorio.", title="Validación")
            return False

        if not self.add_editorial.get():
            Messagebox.show_warning(
                "Selecciona una editorial.", title="Validación")
            return False

        if not self.add_autor.get():
            Messagebox.show_warning("Selecciona un autor.", title="Validación")
            return False

        if not self.add_ubicacion.get():
            Messagebox.show_warning(
                "La ubicación es obligatoria.", title="Validación")
            return False

        return True

    def _validate_update(self) -> bool:
        if not self.update_isbn.get():
            Messagebox.show_warning(
                "Selecciona un registro de la tabla primero.", title="Validación"
            )
            return False

        if not self.update_titulo.get():
            Messagebox.show_warning(
                "El título es obligatorio.", title="Validación")
            return False

        if not self.update_editorial.get():
            Messagebox.show_warning(
                "Selecciona una editorial.", title="Validación")
            return False

        if not self.update_autor.get():
            Messagebox.show_warning("Selecciona un autor.", title="Validación")
            return False

        if not self.update_ubicacion.get():
            Messagebox.show_warning(
                "La ubicación es obligatoria.", title="Validación")
            return False

        return True

    # ─────────────────────────── ACCIONES CRUD ────────────────────────────

    def _insert(self):
        if not self._validate_add():
            return
        try:
            self.add_model.ISBN = self.add_isbn.get()
            self.add_model.Titulo = self.add_titulo.get()
            # Los combos ya actualizan los objetos Editorial y Autor
            self.add_model.Ubicación = self.add_ubicacion.get()
            self.add_model.insert()
            self._update_datatable()
            self._clear_left_form()
            Messagebox.show_info(
                "Libro agregado correctamente.", title="Éxito")
        except Exception as e:
            Messagebox.show_error(f"Error al insertar:\n{e}", title="Error")

    def _update(self):
        if not self._validate_update():
            return
        try:
            self.update_model.Titulo = self.update_titulo.get()
            self.update_model.Ubicación = self.update_ubicacion.get()
            # Los combos ya actualizan los objetos Editorial y Autor
            self.update_model.update()
            self._update_datatable()
            Messagebox.show_info(
                "Libro actualizado correctamente.", title="Éxito")
        except Exception as e:
            Messagebox.show_error(f"Error al actualizar:\n{e}", title="Error")

    def _delete(self):
        if not self.update_isbn.get():
            Messagebox.show_warning(
                "Selecciona un registro de la tabla primero.", title="Validación"
            )
            return

        confirm = Messagebox.yesno(
            f"¿Eliminar el libro con ISBN {self.update_isbn.get()}?",
            title="Confirmar eliminación",
        )
        if confirm not in ["Yes", "Sí", "Ja"]:
            return

        try:
            self.update_model.delete()
            self._update_datatable()
            self._clear_right_form()
            Messagebox.show_info(
                "Libro eliminado correctamente.", title="Éxito")
        except Exception as e:
            Messagebox.show_error(f"Error al eliminar:\n{e}", title="Error")

    # ─────────────────────────── TABLA ────────────────────────────────────

    def _update_datatable(self):
        self.data_table.clear()
        tmp = Libro()
        tmp.set_connection(self.connection)
        self.data_table.insertMany(
            [
                (
                    libro.ISBN,
                    libro.Titulo,
                    libro.Editorial.id,
                    libro.Autor.id,
                    libro.Ubicación,
                )
                for libro in tmp.select()
            ]
        )

    def _on_row_selected(self, values: tuple):
        """Llena el formulario derecho con los datos de la fila seleccionada."""
        if not values:
            return

        isbn, titulo, id_editorial, id_autor, ubicacion = values

        # Sincronizar update_model (PK y FK)
        self.update_model.ISBN = isbn
        self.update_model.Editorial.id = id_editorial
        self.update_model.Autor.id = id_autor

        # Poblar campos del formulario derecho
        self.update_isbn.set(isbn)
        self.update_titulo.set(titulo)
        self.update_editorial.set(str(id_editorial))
        self.update_autor.set(str(id_autor))
        self.update_ubicacion.set(ubicacion)

    def _clear_left_form(self):
        """Limpia el formulario izquierdo tras una inserción exitosa."""
        self.add_isbn.clear()
        self.add_titulo.clear()
        self.add_editorial.set("")
        self.add_autor.set("")
        self.add_ubicacion.clear()

        # Reiniciar add_model
        self.add_model = Libro()
        self.add_model.set_connection(self.connection)

    def _clear_right_form(self):
        """Limpia el formulario derecho tras una eliminación."""
        self.update_isbn.set("")
        self.update_titulo.clear()
        self.update_editorial.set("")
        self.update_autor.set("")
        self.update_ubicacion.clear()

        # Reiniciar update_model
        self.update_model = Libro()
        self.update_model.set_connection(self.connection)

    # ─────────────────────────── CLAVES FK ────────────────────────────────

    def _load_keys(self):
        tmp_editorial = Editorial()
        tmp_editorial.set_connection(self.connection)
        tmp_autor = Autor()
        tmp_autor.set_connection(self.connection)

        self.editorial_keys = [str(ed.id) for ed in tmp_editorial.select()]
        self.autor_keys = [str(au.id) for au in tmp_autor.select()]
