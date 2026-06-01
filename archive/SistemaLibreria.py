import tkinter as tk
from tkinter import ttk

# =========================================
# VENTANA PRINCIPAL
# =========================================

ventana = tk.Tk()

ventana.title("Sistema de Librería ")
ventana.geometry("950x650")

# =========================================
# PESTAÑITAS, el notebook es el contenedor de las pestañas :)
# =========================================

notebook = ttk.Notebook(ventana)
notebook.pack(expand=True, fill="both")

# =========================================
# PESTAÑA LIBROS
# =========================================

frame_libros = ttk.Frame(notebook)
notebook.add(frame_libros, text="Libros")

ttk.Label(frame_libros, text="ISBN").grid(row=0, column=0, padx=10, pady=10)

ttk.Entry(frame_libros, width=30).grid(row=0, column=1)

ttk.Label(frame_libros, text="Título").grid(row=1, column=0, padx=10, pady=10)

ttk.Entry(frame_libros, width=30).grid(row=1, column=1)

ttk.Label(frame_libros, text="Autor").grid(row=2, column=0, padx=10, pady=10)

combo_autor = ttk.Combobox(
    frame_libros,
    width=27,
    values=[
        "Gabriel García Márquez",
        "Isabel Allende",
        "Julio Cortázar"
    ]
)

combo_autor.grid(row=2, column=1)

ttk.Label(frame_libros, text="Editorial").grid(row=3, column=0, padx=10, pady=10)

combo_editorial = ttk.Combobox(
    frame_libros,
    width=27,
    values=[
        "Editorial Alfa",
        "Editorial Luna",
        "Editorial Sol"
    ]
)

combo_editorial.grid(row=3, column=1)

ttk.Label(frame_libros, text="Ubicación").grid(row=4, column=0, padx=10, pady=10)

ttk.Entry(frame_libros, width=30).grid(row=4, column=1)

ttk.Label(frame_libros, text="Stock").grid(row=5, column=0, padx=10, pady=10)

ttk.Entry(frame_libros, width=30).grid(row=5, column=1)

ttk.Label(frame_libros, text="Precio").grid(row=6, column=0, padx=10, pady=10)

ttk.Entry(frame_libros, width=30).grid(row=6, column=1)

ttk.Button(
    frame_libros,
    text="Guardar Libro"
).grid(row=7, column=0, pady=20)

ttk.Button(
    frame_libros,
    text="Limpiar Campos"
).grid(row=7, column=1, pady=20)

# =========================================
# PESTAÑA CLIENTES
# =========================================

frame_clientes = ttk.Frame(notebook)
notebook.add(frame_clientes, text="Clientes")

ttk.Label(frame_clientes, text="Nombre").grid(row=0, column=0, padx=10, pady=10)

ttk.Entry(frame_clientes, width=30).grid(row=0, column=1)

ttk.Label(frame_clientes, text="Apellidos").grid(row=1, column=0, padx=10, pady=10)

ttk.Entry(frame_clientes, width=30).grid(row=1, column=1)

ttk.Label(frame_clientes, text="Correo").grid(row=2, column=0, padx=10, pady=10)

ttk.Entry(frame_clientes, width=30).grid(row=2, column=1)

ttk.Label(frame_clientes, text="Celular").grid(row=3, column=0, padx=10, pady=10)

ttk.Entry(frame_clientes, width=30).grid(row=3, column=1)

ttk.Button(
    frame_clientes,
    text="Registrar Cliente"
).grid(row=4, column=0, pady=20)

# =========================================
# PESTAÑA MODIFICAR
# =========================================

frame_modificar = ttk.Frame(notebook)
notebook.add(frame_modificar, text="Modificar")

ttk.Label(frame_modificar, text="Buscar ISBN").grid(row=0, column=0, padx=10, pady=10)

ttk.Entry(frame_modificar, width=30).grid(row=0, column=1)

ttk.Button(
    frame_modificar,
    text="Buscar"
).grid(row=1, column=0, pady=20)

ttk.Button(
    frame_modificar,
    text="Modificar Datos"
).grid(row=1, column=1, pady=20)

# =========================================
# PESTAÑA REPORTES
# =========================================

frame_reportes = ttk.Frame(notebook)
notebook.add(frame_reportes, text="Reportes")

ttk.Button(
    frame_reportes,
    text="Mostrar libros vendidos por fecha"
).grid(row=0, column=0, padx=20, pady=20)

ttk.Button(
    frame_reportes,
    text="Libros con stock menor a 5"
).grid(row=1, column=0, padx=20, pady=20)

ttk.Button(
    frame_reportes,
    text="Libros con autor y editorial"
).grid(row=2, column=0, padx=20, pady=20)

# =========================================
# EJECUTAR VENTANA
# =========================================

ventana.mainloop()