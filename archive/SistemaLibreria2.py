import tkinter as tk
from tkinter import ttk, messagebox

ventana = tk.Tk()
ventana.title("Sistema de Librería 2")
ventana.geometry("1050x680")

# =========================
# ESTILO
# =========================

style = ttk.Style()
style.theme_use("clam")

style.configure("TNotebook.Tab", font=("Arial", 11, "bold"), padding=[12, 6])
style.configure("TLabel", font=("Arial", 11))
style.configure("TButton", font=("Arial", 10, "bold"))

titulo = ttk.Label(
    ventana,
    text="Sistema de Librería - Prototipo 2",
    font=("Arial", 20, "bold")
)
titulo.pack(pady=12)

notebook = ttk.Notebook(ventana)
notebook.pack(expand=True, fill="both", padx=15, pady=10)

# =========================
# FUNCIONES DE PROTOTIPO
# =========================

def mensaje_guardar():
    messagebox.showinfo("Registro", "Datos guardados en el prototipo.")

def limpiar_campos(lista_campos):
    for campo in lista_campos:
        campo.delete(0, tk.END)

# =========================
# PESTAÑA LIBROS
# =========================

frame_libros = ttk.Frame(notebook)
notebook.add(frame_libros, text="Registro de libros")

contenedor_libros = ttk.LabelFrame(frame_libros, text="Datos del libro")
contenedor_libros.pack(fill="x", padx=20, pady=15)

ttk.Label(contenedor_libros, text="ISBN").grid(row=0, column=0, padx=10, pady=10, sticky="w")
txt_isbn = ttk.Entry(contenedor_libros, width=35)
txt_isbn.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(contenedor_libros, text="Título").grid(row=1, column=0, padx=10, pady=10, sticky="w")
txt_titulo = ttk.Entry(contenedor_libros, width=35)
txt_titulo.grid(row=1, column=1, padx=10, pady=10)

ttk.Label(contenedor_libros, text="Autor").grid(row=2, column=0, padx=10, pady=10, sticky="w")
combo_autor = ttk.Combobox(
    contenedor_libros,
    width=32,
    values=[
        "Edgar Allan Poe",
        "Osamu Dazai",
        "Franz Kafka",
        "Mary Shelley",
        "H. P. Lovecraft"
    ]
)
combo_autor.grid(row=2, column=1, padx=10, pady=10)

ttk.Label(contenedor_libros, text="Editorial").grid(row=3, column=0, padx=10, pady=10, sticky="w")
combo_editorial = ttk.Combobox(
    contenedor_libros,
    width=32,
    values=[
        "Pollito Negro Editorial",
        "Pollito Gótico Books",
        "Editorial Alas de Cuervo",
        "Pollitos del Abismo",
        "Libros Medianoche"
    ]
)
combo_editorial.grid(row=3, column=1, padx=10, pady=10)

ttk.Label(contenedor_libros, text="Ubicación").grid(row=4, column=0, padx=10, pady=10, sticky="w")
txt_ubicacion = ttk.Entry(contenedor_libros, width=35)
txt_ubicacion.grid(row=4, column=1, padx=10, pady=10)

ttk.Label(contenedor_libros, text="Stock").grid(row=5, column=0, padx=10, pady=10, sticky="w")
txt_stock = ttk.Entry(contenedor_libros, width=35)
txt_stock.grid(row=5, column=1, padx=10, pady=10)

ttk.Label(contenedor_libros, text="Precio").grid(row=6, column=0, padx=10, pady=10, sticky="w")
txt_precio = ttk.Entry(contenedor_libros, width=35)
txt_precio.grid(row=6, column=1, padx=10, pady=10)

ttk.Button(contenedor_libros, text="Guardar libro", command=mensaje_guardar).grid(row=7, column=0, padx=10, pady=15)
ttk.Button(
    contenedor_libros,
    text="Limpiar",
    command=lambda: limpiar_campos([txt_isbn, txt_titulo, txt_ubicacion, txt_stock, txt_precio])
).grid(row=7, column=1, padx=10, pady=15)

tabla_libros = ttk.Treeview(
    frame_libros,
    columns=("ISBN", "Titulo", "Autor", "Editorial", "Stock", "Precio"),
    show="headings",
    height=6
)

tabla_libros.heading("ISBN", text="ISBN")
tabla_libros.heading("Titulo", text="Título")
tabla_libros.heading("Autor", text="Autor")
tabla_libros.heading("Editorial", text="Editorial")
tabla_libros.heading("Stock", text="Stock")
tabla_libros.heading("Precio", text="Precio")

tabla_libros.pack(fill="x", padx=20, pady=10)
tabla_libros.insert("", "end", values=("978-0141439815", "El cuervo", "Edgar Allan Poe", "Pollito Gótico Books", 4, "$120"))
tabla_libros.insert("", "end", values=("978-0811204811", "Indigno de ser humano", "Osamu Dazai", "Pollitos del Abismo", 8, "$180"))
tabla_libros.insert("", "end", values=("978-0805209990", "La metamorfosis", "Franz Kafka", "Editorial Alas de Cuervo", 3, "$150"))

# =========================
# PESTAÑA CLIENTES
# =========================

frame_clientes = ttk.Frame(notebook)
notebook.add(frame_clientes, text="Registro de clientes")

contenedor_clientes = ttk.LabelFrame(frame_clientes, text="Datos del cliente")
contenedor_clientes.pack(fill="x", padx=20, pady=15)

ttk.Label(contenedor_clientes, text="Nombre").grid(row=0, column=0, padx=10, pady=10, sticky="w")
txt_nombre = ttk.Entry(contenedor_clientes, width=35)
txt_nombre.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(contenedor_clientes, text="Apellidos").grid(row=1, column=0, padx=10, pady=10, sticky="w")
txt_apellidos = ttk.Entry(contenedor_clientes, width=35)
txt_apellidos.grid(row=1, column=1, padx=10, pady=10)

ttk.Label(contenedor_clientes, text="Correo electrónico").grid(row=2, column=0, padx=10, pady=10, sticky="w")
txt_correo = ttk.Entry(contenedor_clientes, width=35)
txt_correo.grid(row=2, column=1, padx=10, pady=10)

ttk.Label(contenedor_clientes, text="Número celular").grid(row=3, column=0, padx=10, pady=10, sticky="w")
txt_celular = ttk.Entry(contenedor_clientes, width=35)
txt_celular.grid(row=3, column=1, padx=10, pady=10)

ttk.Button(contenedor_clientes, text="Registrar cliente", command=mensaje_guardar).grid(row=4, column=0, padx=10, pady=15)
ttk.Button(
    contenedor_clientes,
    text="Limpiar",
    command=lambda: limpiar_campos([txt_nombre, txt_apellidos, txt_correo, txt_celular])
).grid(row=4, column=1, padx=10, pady=15)

# =========================
# PESTAÑA COMPRAS
# =========================

frame_compras = ttk.Frame(notebook)
notebook.add(frame_compras, text="Compras")

contenedor_compras = ttk.LabelFrame(frame_compras, text="Datos de compra")
contenedor_compras.pack(fill="x", padx=20, pady=15)

ttk.Label(contenedor_compras, text="ID compra").grid(row=0, column=0, padx=10, pady=10)
ttk.Entry(contenedor_compras, width=35).grid(row=0, column=1, padx=10, pady=10)

ttk.Label(contenedor_compras, text="Fecha").grid(row=1, column=0, padx=10, pady=10)
ttk.Entry(contenedor_compras, width=35).grid(row=1, column=1, padx=10, pady=10)

ttk.Label(contenedor_compras, text="Cliente").grid(row=2, column=0, padx=10, pady=10)
ttk.Entry(contenedor_compras, width=35).grid(row=2, column=1, padx=10, pady=10)

ttk.Label(contenedor_compras, text="Libro / ISBN").grid(row=3, column=0, padx=10, pady=10)
ttk.Combobox(
    contenedor_compras,
    width=32,
    values=[
        "978-0141439815 - El cuervo",
        "978-0811204811 - Indigno de ser humano",
        "978-0805209990 - La metamorfosis"
    ]
).grid(row=3, column=1, padx=10, pady=10)

ttk.Label(contenedor_compras, text="Cantidad").grid(row=4, column=0, padx=10, pady=10)
ttk.Entry(contenedor_compras, width=35).grid(row=4, column=1, padx=10, pady=10)

ttk.Label(contenedor_compras, text="Total compra").grid(row=5, column=0, padx=10, pady=10)
ttk.Entry(contenedor_compras, width=35).grid(row=5, column=1, padx=10, pady=10)

ttk.Button(contenedor_compras, text="Registrar compra", command=mensaje_guardar).grid(row=6, column=0, padx=10, pady=15)

# =========================
# PESTAÑA MODIFICAR
# =========================

frame_modificar = ttk.Frame(notebook)
notebook.add(frame_modificar, text="Modificar")

contenedor_modificar = ttk.LabelFrame(frame_modificar, text="Modificar datos de libro")
contenedor_modificar.pack(fill="x", padx=20, pady=15)

ttk.Label(contenedor_modificar, text="Buscar ISBN").grid(row=0, column=0, padx=10, pady=10)
ttk.Entry(contenedor_modificar, width=35).grid(row=0, column=1, padx=10, pady=10)

ttk.Button(contenedor_modificar, text="Buscar").grid(row=0, column=2, padx=10, pady=10)

ttk.Label(contenedor_modificar, text="Nuevo título").grid(row=1, column=0, padx=10, pady=10)
ttk.Entry(contenedor_modificar, width=35).grid(row=1, column=1, padx=10, pady=10)

ttk.Label(contenedor_modificar, text="Nuevo stock").grid(row=2, column=0, padx=10, pady=10)
ttk.Entry(contenedor_modificar, width=35).grid(row=2, column=1, padx=10, pady=10)

ttk.Label(contenedor_modificar, text="Nuevo precio").grid(row=3, column=0, padx=10, pady=10)
ttk.Entry(contenedor_modificar, width=35).grid(row=3, column=1, padx=10, pady=10)

ttk.Button(contenedor_modificar, text="Actualizar datos", command=mensaje_guardar).grid(row=4, column=1, padx=10, pady=15)

# =========================
# PESTAÑA REPORTES
# =========================

frame_reportes = ttk.Frame(notebook)
notebook.add(frame_reportes, text="Reportes")

contenedor_reportes = ttk.LabelFrame(frame_reportes, text="Reportes solicitados")
contenedor_reportes.pack(fill="x", padx=20, pady=15)

ttk.Label(contenedor_reportes, text="Fecha del pedido").grid(row=0, column=0, padx=10, pady=10)
ttk.Entry(contenedor_reportes, width=25).grid(row=0, column=1, padx=10, pady=10)

ttk.Button(contenedor_reportes, text="Libros vendidos por fecha", command=mensaje_guardar).grid(row=0, column=2, padx=10, pady=10)
ttk.Button(contenedor_reportes, text="Stock menor a 5", command=mensaje_guardar).grid(row=1, column=0, padx=10, pady=10)
ttk.Button(contenedor_reportes, text="Libros con autor y editorial", command=mensaje_guardar).grid(row=1, column=1, padx=10, pady=10)

tabla_reportes = ttk.Treeview(
    frame_reportes,
    columns=("ISBN", "Titulo", "Autor", "Editorial", "Stock"),
    show="headings",
    height=8
)

tabla_reportes.heading("ISBN", text="ISBN")
tabla_reportes.heading("Titulo", text="Título")
tabla_reportes.heading("Autor", text="Autor")
tabla_reportes.heading("Editorial", text="Editorial")
tabla_reportes.heading("Stock", text="Stock")

tabla_reportes.pack(fill="x", padx=20, pady=15)

tabla_reportes.insert("", "end", values=("978-0141439815", "El cuervo", "Edgar Allan Poe", "Pollito Gótico Books", 4))
tabla_reportes.insert("", "end", values=("978-0805209990", "La metamorfosis", "Franz Kafka", "Editorial Alas de Cuervo", 3))

ventana.mainloop()