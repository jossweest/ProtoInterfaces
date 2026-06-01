import tkinter as tk
from tkinter import ttk, messagebox

ventana = tk.Tk()
ventana.title("Librería Los Pollitos 🐣")
ventana.geometry("1000x650")

style = ttk.Style()
style.theme_use("clam")

style.configure("TNotebook.Tab", font=("Arial", 11, "bold"), padding=[10, 5])
style.configure("TLabel", font=("Arial", 11))
style.configure("TButton", font=("Arial", 10, "bold"))

def mensaje(texto):
    messagebox.showinfo("Librería Los Pollitos 🐣", texto)

def limpiar(campos):
    for campo in campos:
        campo.delete(0, tk.END)

titulo = ttk.Label(
    ventana,
    text="Librería Los Pollitos 🐣",
    font=("Arial", 20, "bold")
)
titulo.pack(pady=10)

notebook = ttk.Notebook(ventana)
notebook.pack(expand=True, fill="both", padx=15, pady=10)
# ======================================
# PESTAÑA LIBROS
# ======================================

frame_libros = ttk.Frame(notebook)
notebook.add(frame_libros, text="Libros")

caja_libros = ttk.LabelFrame(frame_libros, text="Registro de libros")
caja_libros.pack(fill="x", padx=20, pady=15)

ttk.Label(caja_libros, text="ISBN").grid(row=0, column=0, padx=10, pady=8, sticky="w")
txt_isbn = ttk.Entry(caja_libros, width=35)
txt_isbn.grid(row=0, column=1, padx=10, pady=8)

ttk.Label(caja_libros, text="Título").grid(row=1, column=0, padx=10, pady=8, sticky="w")
txt_titulo = ttk.Entry(caja_libros, width=35)
txt_titulo.grid(row=1, column=1, padx=10, pady=8)

ttk.Label(caja_libros, text="Autor").grid(row=2, column=0, padx=10, pady=8, sticky="w")
combo_autor = ttk.Combobox(
    caja_libros,
    width=32,
    values=[
        "Edgar Allan Poe",
        "Osamu Dazai",
        "Franz Kafka",
        "Mary Shelley"
    ]
)
combo_autor.grid(row=2, column=1, padx=10, pady=8)

ttk.Label(caja_libros, text="Editorial").grid(row=3, column=0, padx=10, pady=8, sticky="w")
combo_editorial = ttk.Combobox(
    caja_libros,
    width=32,
    values=[
        "Pollito Editorial",
        "Pollito Clásicos",
        "Editorial Cuervo",
        "Libros Medianoche"
    ]
)
combo_editorial.grid(row=3, column=1, padx=10, pady=8)

ttk.Label(caja_libros, text="Ubicación").grid(row=4, column=0, padx=10, pady=8, sticky="w")
txt_ubicacion = ttk.Entry(caja_libros, width=35)
txt_ubicacion.grid(row=4, column=1, padx=10, pady=8)

ttk.Label(caja_libros, text="Stock").grid(row=5, column=0, padx=10, pady=8, sticky="w")
txt_stock = ttk.Entry(caja_libros, width=35)
txt_stock.grid(row=5, column=1, padx=10, pady=8)

ttk.Label(caja_libros, text="Precio").grid(row=6, column=0, padx=10, pady=8, sticky="w")
txt_precio = ttk.Entry(caja_libros, width=35)
txt_precio.grid(row=6, column=1, padx=10, pady=8)

ttk.Button(
    caja_libros,
    text="Guardar libro",
    command=lambda: mensaje("Libro guardado en el prototipo.")
).grid(row=7, column=0, padx=10, pady=15)

ttk.Button(
    caja_libros,
    text="Limpiar",
    command=lambda: limpiar([txt_isbn, txt_titulo, txt_ubicacion, txt_stock, txt_precio])
).grid(row=7, column=1, padx=10, pady=15)

tabla_libros = ttk.Treeview(
    frame_libros,
    columns=("ISBN", "Título", "Autor", "Editorial", "Stock"),
    show="headings",
    height=5
)

tabla_libros.heading("ISBN", text="ISBN")
tabla_libros.heading("Título", text="Título")
tabla_libros.heading("Autor", text="Autor")
tabla_libros.heading("Editorial", text="Editorial")
tabla_libros.heading("Stock", text="Stock")

tabla_libros.pack(fill="x", padx=20, pady=10)

tabla_libros.insert("", "end", values=("978-0141439815", "El cuervo", "Edgar Allan Poe", "Editorial Cuervo", 4))
tabla_libros.insert("", "end", values=("978-0811204811", "Indigno de ser humano", "Osamu Dazai", "Pollito Clásicos", 8))
tabla_libros.insert("", "end", values=("978-0805209990", "La metamorfosis", "Franz Kafka", "Libros Medianoche", 3))

# ======================================
# PESTAÑA CLIENTES
# ======================================

frame_clientes = ttk.Frame(notebook)
notebook.add(frame_clientes, text="Clientes")

caja_clientes = ttk.LabelFrame(frame_clientes, text="Registro de clientes")
caja_clientes.pack(fill="x", padx=20, pady=15)

ttk.Label(caja_clientes, text="Nombre").grid(row=0, column=0, padx=10, pady=8, sticky="w")
txt_nombre = ttk.Entry(caja_clientes, width=35)
txt_nombre.grid(row=0, column=1, padx=10, pady=8)

ttk.Label(caja_clientes, text="Apellidos").grid(row=1, column=0, padx=10, pady=8, sticky="w")
txt_apellidos = ttk.Entry(caja_clientes, width=35)
txt_apellidos.grid(row=1, column=1, padx=10, pady=8)

ttk.Label(caja_clientes, text="Correo electrónico").grid(row=2, column=0, padx=10, pady=8, sticky="w")
txt_correo = ttk.Entry(caja_clientes, width=35)
txt_correo.grid(row=2, column=1, padx=10, pady=8)

ttk.Label(caja_clientes, text="Número celular").grid(row=3, column=0, padx=10, pady=8, sticky="w")
txt_celular = ttk.Entry(caja_clientes, width=35)
txt_celular.grid(row=3, column=1, padx=10, pady=8)

ttk.Button(
    caja_clientes,
    text="Registrar cliente",
    command=lambda: mensaje("Cliente registrado en el prototipo.")
).grid(row=4, column=0, padx=10, pady=15)

ttk.Button(
    caja_clientes,
    text="Limpiar",
    command=lambda: limpiar([txt_nombre, txt_apellidos, txt_correo, txt_celular])
).grid(row=4, column=1, padx=10, pady=15)

# ======================================
# PESTAÑA COMPRAS
# ======================================

frame_compras = ttk.Frame(notebook)
notebook.add(frame_compras, text="Compras")

caja_compras = ttk.LabelFrame(frame_compras, text="Registro de compras")
caja_compras.pack(fill="x", padx=20, pady=15)

ttk.Label(caja_compras, text="ID compra").grid(row=0, column=0, padx=10, pady=8, sticky="w")
ttk.Entry(caja_compras, width=35).grid(row=0, column=1, padx=10, pady=8)

ttk.Label(caja_compras, text="Fecha").grid(row=1, column=0, padx=10, pady=8, sticky="w")
ttk.Entry(caja_compras, width=35).grid(row=1, column=1, padx=10, pady=8)

ttk.Label(caja_compras, text="ID Cliente").grid(row=2, column=0, padx=10, pady=8, sticky="w")
ttk.Entry(caja_compras, width=35).grid(row=2, column=1, padx=10, pady=8)

ttk.Label(caja_compras, text="Libro / ISBN").grid(row=3, column=0, padx=10, pady=8, sticky="w")

ttk.Combobox(
    caja_compras,
    width=45,
    values=[
        "978-0141439815 - El cuervo - Edgar Allan Poe",
        "978-0811204811 - Indigno de ser humano - Osamu Dazai",
        "978-0805209990 - La metamorfosis - Franz Kafka",
        "978-0141439471 - Frankenstein - Mary Shelley"
    ]
).grid(row=3, column=1, padx=10, pady=8)

ttk.Label(caja_compras, text="Cantidad").grid(row=4, column=0, padx=10, pady=8, sticky="w")
ttk.Entry(caja_compras, width=35).grid(row=4, column=1, padx=10, pady=8)

ttk.Label(caja_compras, text="Precio").grid(row=5, column=0, padx=10, pady=8, sticky="w")
ttk.Entry(caja_compras, width=35).grid(row=5, column=1, padx=10, pady=8)

ttk.Button(
    caja_compras,
    text="Registrar compra",
    command=lambda: mensaje("Compra registrada en el prototipo.")
).grid(row=6, column=0, padx=10, pady=15)

# ======================================
# PESTAÑA MODIFICAR
# ======================================
frame_modificar = ttk.Frame(notebook)
notebook.add(frame_modificar, text="Modificar")

caja_modificar = ttk.LabelFrame(frame_modificar, text="Modificar libro")
caja_modificar.pack(fill="x", padx=20, pady=15)

ttk.Label(caja_modificar, text="Buscar ISBN").grid(row=0, column=0, padx=10, pady=8, sticky="w")
ttk.Entry(caja_modificar, width=35).grid(row=0, column=1, padx=10, pady=8)

ttk.Button(caja_modificar, text="Buscar").grid(row=0, column=2, padx=10, pady=8)

ttk.Label(caja_modificar, text="Nuevo stock").grid(row=1, column=0, padx=10, pady=8, sticky="w")
ttk.Entry(caja_modificar, width=35).grid(row=1, column=1, padx=10, pady=8)

ttk.Label(caja_modificar, text="Nuevo precio").grid(row=2, column=0, padx=10, pady=8, sticky="w")
ttk.Entry(caja_modificar, width=35).grid(row=2, column=1, padx=10, pady=8)

ttk.Button(
    caja_modificar,
    text="Modificar datos",
    command=lambda: mensaje("Datos modificados en el prototipo.")
).grid(row=3, column=1, padx=10, pady=15)

# ======================================
# PESTAÑA REPORTES
# ======================================

frame_reportes = ttk.Frame(notebook)
notebook.add(frame_reportes, text="Reportes")

caja_reportes = ttk.LabelFrame(frame_reportes, text="Reportes")
caja_reportes.pack(fill="x", padx=20, pady=15)

ttk.Label(caja_reportes, text="Fecha del pedido").grid(row=0, column=0, padx=10, pady=8, sticky="w")
ttk.Entry(caja_reportes, width=25).grid(row=0, column=1, padx=10, pady=8)

ttk.Button(
    caja_reportes,
    text="Libros por fecha"
).grid(row=0, column=2, padx=10, pady=8)

ttk.Button(
    caja_reportes,
    text="Stock menor a 5"
).grid(row=1, column=0, padx=10, pady=8)

ttk.Button(
    caja_reportes,
    text="Autor y editorial"
).grid(row=1, column=1, padx=10, pady=8)

tabla_reportes = ttk.Treeview(
    frame_reportes,
    columns=("ISBN", "Título", "Autor", "Editorial", "Stock"),
    show="headings",
    height=6
)

tabla_reportes.heading("ISBN", text="ISBN")
tabla_reportes.heading("Título", text="Título")
tabla_reportes.heading("Autor", text="Autor")
tabla_reportes.heading("Editorial", text="Editorial")
tabla_reportes.heading("Stock", text="Stock")

tabla_reportes.pack(fill="x", padx=20, pady=15)

tabla_reportes.insert("", "end", values=("978-0141439815", "El cuervo", "Edgar Allan Poe", "Editorial Cuervo", 4))
tabla_reportes.insert("", "end", values=("978-0805209990", "La metamorfosis", "Franz Kafka", "Libros Medianoche", 3))

ventana.mainloop()