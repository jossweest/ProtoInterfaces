from src.model.Model import Model
from src.model.Autor import Autor
from src.model.Cliente import Cliente
from src.model.CompraCabecera import CompraCabecera
from src.model.CompraDetalle import CompraDetalle
from src.model.Editorial import Editorial
from src.model.Ejemplares import Ejemplares
from src.model.Libro import Libro
from src.utils.config import config
from pathlib import Path
from src.backend.PostgresqlConnection import PostgresqlConnection
from typing import List


def main():

    db_config = config(
        file=Path.cwd() / "config.ini",
        section="db"
    )

    psql_connection = PostgresqlConnection()
    psql_connection.connect(**db_config)

    authors: List[Autor] = []

    # 1 - Franz Kafka (Metamorfosis)
    author1 = Autor()
    author1.Nombre = "Franz Kafka"
    authors.append(author1)

    # 2 - Margaret Atwood (El cuento de la criada)
    author2 = Autor()
    author2.Nombre = "Margaret Atwood"
    authors.append(author2)

    # 3 - Inio Asano (Oyasumi Punpun)
    author3 = Autor()
    author3.Nombre = "Inio Asano"
    authors.append(author3)

    # 4 - Harlan Ellison (No tengo boca y debo gritar)
    author4 = Autor()
    author4.Nombre = "Harlan Ellison"
    authors.append(author4)

    # 5 - George Orwell (1984)
    author5 = Autor()
    author5.Nombre = "George Orwell"
    authors.append(author5)

    # 6 - J.K. Rowling (Harry Potter)
    author6 = Autor()
    author6.Nombre = "J.K. Rowling"
    authors.append(author6)

    # 7 - Stephen King (El resplandor)
    author7 = Autor()
    author7.Nombre = "Stephen King"
    authors.append(author7)

    # 8 - Agatha Christie (Asesinato en el Oriente Expreso)
    author8 = Autor()
    author8.Nombre = "Agatha Christie"
    authors.append(author8)

    # 9 - Paulo Coelho (El Alquimista)
    author9 = Autor()
    author9.Nombre = "Paulo Coelho"
    authors.append(author9)

    # 10 - Isaac Asimov (Fundación)
    author10 = Autor()
    author10.Nombre = "Isaac Asimov"
    authors.append(author10)

    # 11 - Mary Shelley (Frankenstein)
    author11 = Autor()
    author11.Nombre = "Mary Shelley"
    authors.append(author11)

    # 12 - Julio Cortázar (Rayuela)
    author12 = Autor()
    author12.Nombre = "Julio Cortázar"
    authors.append(author12)

    # 13 - Gabriel García Márquez (Cien años de soledad)
    author13 = Autor()
    author13.Nombre = "Gabriel García Márquez"
    authors.append(author13)

    # 14 - J.R.R. Tolkien (El Señor de los Anillos)
    author14 = Autor()
    author14.Nombre = "J.R.R. Tolkien"
    authors.append(author14)

    # 15 - Oscar Wilde (El retrato de Dorian Gray)
    author15 = Autor()
    author15.Nombre = "Oscar Wilde"
    authors.append(author15)

    # Insertar todos los autores
    i = 1
    for author in authors:
        author.id = i
        i += 1
        author.set_connection(psql_connection)
        author.insert()

    editoriales: List[Editorial] = []

    # Crear editoriales
    editorial1 = Editorial()
    editorial1.Nombre = "Penguin Classics"
    editoriales.append(editorial1)

    editorial2 = Editorial()
    editorial2.Nombre = "Doubleday"
    editoriales.append(editorial2)

    editorial3 = Editorial()
    editorial3.Nombre = "Planeta"
    editoriales.append(editorial3)

    editorial4 = Editorial()
    editorial4.Nombre = "Alfaguara"
    editoriales.append(editorial4)

    editorial5 = Editorial()
    editorial5.Nombre = "Minotauro"
    editoriales.append(editorial5)

    editorial6 = Editorial()
    editorial6.Nombre = "Tusquets"
    editoriales.append(editorial6)

    editorial7 = Editorial()
    editorial7.Nombre = "Seix Barral"
    editoriales.append(editorial7)

    editorial8 = Editorial()
    editorial8.Nombre = "Anagrama"
    editoriales.append(editorial8)

    editorial9 = Editorial()
    editorial9.Nombre = "Espasa"
    editoriales.append(editorial9)

    editorial10 = Editorial()
    editorial10.Nombre = "Grijalbo"
    editoriales.append(editorial10)

    editorial11 = Editorial()
    editorial11.Nombre = "Edhasa"
    editoriales.append(editorial11)

    editorial12 = Editorial()
    editorial12.Nombre = "Plaza & Janés"
    editoriales.append(editorial12)

    editorial13 = Editorial()
    editorial13.Nombre = "Ediciones SM"
    editoriales.append(editorial13)

    editorial14 = Editorial()
    editorial14.Nombre = "Bloomsbury"
    editoriales.append(editorial14)

    editorial15 = Editorial()
    editorial15.Nombre = "Harper Perennial"
    editoriales.append(editorial15)

    # Insertar editoriales
    i = 1
    for editorial in editoriales:
        editorial.id = i
        i += 1
        editorial.set_connection(psql_connection)
        editorial.insert()

    # Libros
    books: List[Libro] = []

    # 1 - Metamorfosis (Franz Kafka)
    book1 = Libro()
    book1.ISBN = "978-0-14-118008-6"
    book1.Titulo = "Metamorfosis"
    book1.Editorial = authors[0]  # Franz Kafka
    book1.Autor = authors[0]
    book1.Ubicación = "Sección Clásicos A1"
    books.append(book1)

    # 2 - El cuento de la criada (Margaret Atwood)
    book2 = Libro()
    book2.ISBN = "978-0-385-49081-8"
    book2.Titulo = "El cuento de la criada"
    book2.Editorial = authors[1]  # Margaret Atwood
    book2.Autor = authors[1]
    book2.Ubicación = "Sección Ficción B2"
    books.append(book2)

    # 3 - Oyasumi Punpun (Inio Asano)
    book3 = Libro()
    book3.ISBN = "978-4-7575-2486-5"
    book3.Titulo = "Oyasumi Punpun"
    book3.Editorial = authors[2]  # Inio Asano
    book3.Autor = authors[2]
    book3.Ubicación = "Sección Manga C3"
    books.append(book3)

    # 4 - No tengo boca y debo gritar (Harlan Ellison)
    book4 = Libro()
    book4.ISBN = "978-0-14-009876-5"
    book4.Titulo = "No tengo boca y debo gritar"
    book4.Editorial = authors[3]  # Harlan Ellison
    book4.Autor = authors[3]
    book4.Ubicación = "Sección Ciencia Ficción D1"
    books.append(book4)

    # 5 - 1984 (George Orwell)
    book5 = Libro()
    book5.ISBN = "978-0-452-26234-2"
    book5.Titulo = "1984"
    book5.Editorial = authors[4]  # George Orwell
    book5.Autor = authors[4]
    book5.Ubicación = "Sección Clásicos A2"
    books.append(book5)

    # 6 - Harry Potter (J.K. Rowling)
    book6 = Libro()
    book6.ISBN = "978-0-439-13959-0"
    book6.Titulo = "Harry Potter y la Piedra Filosofal"
    book6.Editorial = authors[5]  # J.K. Rowling
    book6.Autor = authors[5]
    book6.Ubicación = "Sección Fantasía E1"
    books.append(book6)

    # 7 - El resplandor (Stephen King)
    book7 = Libro()
    book7.ISBN = "978-0-385-33312-0"
    book7.Titulo = "El resplandor"
    book7.Editorial = authors[6]  # Stephen King
    book7.Autor = authors[6]
    book7.Ubicación = "Sección Terror F2"
    books.append(book7)

    # 8 - Asesinato en el Oriente Expreso (Agatha Christie)
    book8 = Libro()
    book8.ISBN = "978-0-062-07343-2"
    book8.Titulo = "Asesinato en el Oriente Expreso"
    book8.Editorial = authors[7]  # Agatha Christie
    book8.Autor = authors[7]
    book8.Ubicación = "Sección Misterio G1"
    books.append(book8)

    # 9 - El Alquimista (Paulo Coelho)
    book9 = Libro()
    book9.ISBN = "978-0-06-085396-8"
    book9.Titulo = "El Alquimista"
    book9.Editorial = authors[8]  # Paulo Coelho
    book9.Autor = authors[8]
    book9.Ubicación = "Sección Desarrollo H3"
    books.append(book9)

    # 10 - Fundación (Isaac Asimov)
    book10 = Libro()
    book10.ISBN = "978-0-553-29438-0"
    book10.Titulo = "Fundación"
    book10.Editorial = authors[9]  # Isaac Asimov
    book10.Autor = authors[9]
    book10.Ubicación = "Sección Ciencia Ficción D2"
    books.append(book10)

    # 11 - Frankenstein (Mary Shelley)
    book11 = Libro()
    book11.ISBN = "978-0-14-143984-8"
    book11.Titulo = "Frankenstein"
    book11.Editorial = authors[10]  # Mary Shelley
    book11.Autor = authors[10]
    book11.Ubicación = "Sección Clásicos A3"
    books.append(book11)

    # 12 - Rayuela (Julio Cortázar)
    book12 = Libro()
    book12.ISBN = "978-987-04-0032-3"
    book12.Titulo = "Rayuela"
    book12.Editorial = authors[11]  # Julio Cortázar
    book12.Autor = authors[11]
    book12.Ubicación = "Sección Literatura Latinoamericana I1"
    books.append(book12)

    # 13 - Cien años de soledad (Gabriel García Márquez)
    book13 = Libro()
    book13.ISBN = "978-84-322-3476-4"
    book13.Titulo = "Cien años de soledad"
    book13.Editorial = authors[12]  # Gabriel García Márquez
    book13.Autor = authors[12]
    book13.Ubicación = "Sección Literatura Latinoamericana I2"
    books.append(book13)

    # 14 - El Señor de los Anillos (J.R.R. Tolkien)
    book14 = Libro()
    book14.ISBN = "978-0-544-00674-8"
    book14.Titulo = "El Señor de los Anillos"
    book14.Editorial = authors[13]  # J.R.R. Tolkien
    book14.Autor = authors[13]
    book14.Ubicación = "Sección Fantasía E2"
    books.append(book14)

    # 15 - El retrato de Dorian Gray (Oscar Wilde)
    book15 = Libro()
    book15.ISBN = "978-0-14-143957-2"
    book15.Titulo = "El retrato de Dorian Gray"
    book15.Editorial = authors[14]  # Oscar Wilde
    book15.Autor = authors[14]
    book15.Ubicación = "Sección Clásicos A4"
    books.append(book15)

    # Insertar todos los libros
    for book in books:
        book.set_connection(psql_connection)
        book.insert()

    # Clientes
    clientes: List[Cliente] = []

    # 1
    cliente1 = Cliente()
    cliente1.Nombre = "Juan"
    cliente1.Apellidos = "García López"
    cliente1.CorreoElectronico = "juan.garcia@email.com"
    cliente1.NumCelular = "+52 55 1234 5678"
    clientes.append(cliente1)

    # 2
    cliente2 = Cliente()
    cliente2.Nombre = "María"
    cliente2.Apellidos = "Rodríguez Martínez"
    cliente2.CorreoElectronico = "maria.rodriguez@email.com"
    cliente2.NumCelular = "+52 55 2345 6789"
    clientes.append(cliente2)

    # 3
    cliente3 = Cliente()
    cliente3.Nombre = "Carlos"
    cliente3.Apellidos = "Fernández Gómez"
    cliente3.CorreoElectronico = "carlos.fernandez@email.com"
    cliente3.NumCelular = "+52 33 3456 7890"
    clientes.append(cliente3)

    # 4
    cliente4 = Cliente()
    cliente4.Nombre = "Ana"
    cliente4.Apellidos = "López Sánchez"
    cliente4.CorreoElectronico = "ana.lopez@email.com"
    cliente4.NumCelular = "+52 81 4567 8901"
    clientes.append(cliente4)

    # 5
    cliente5 = Cliente()
    cliente5.Nombre = "Pedro"
    cliente5.Apellidos = "Moreno García"
    cliente5.CorreoElectronico = "pedro.moreno@email.com"
    cliente5.NumCelular = "+52 662 5678 9012"
    clientes.append(cliente5)

    # 6
    cliente6 = Cliente()
    cliente6.Nombre = "Isabel"
    cliente6.Apellidos = "Jiménez Díaz"
    cliente6.CorreoElectronico = "isabel.jimenez@email.com"
    cliente6.NumCelular = "+52 228 6789 0123"
    clientes.append(cliente6)

    # 7
    cliente7 = Cliente()
    cliente7.Nombre = "Miguel"
    cliente7.Apellidos = "Ruiz Ortiz"
    cliente7.CorreoElectronico = "miguel.ruiz@email.com"
    cliente7.NumCelular = "+52 614 7890 1234"
    clientes.append(cliente7)

    # 8
    cliente8 = Cliente()
    cliente8.Nombre = "Laura"
    cliente8.Apellidos = "Torres Romero"
    cliente8.CorreoElectronico = "laura.torres@email.com"
    cliente8.NumCelular = "+52 222 8901 2345"
    clientes.append(cliente8)

    # 9
    cliente9 = Cliente()
    cliente9.Nombre = "Rafael"
    cliente9.Apellidos = "Vargas Castro"
    cliente9.CorreoElectronico = "rafael.vargas@email.com"
    cliente9.NumCelular = "+52 411 9012 3456"
    clientes.append(cliente9)

    # 10
    cliente10 = Cliente()
    cliente10.Nombre = "Sofía"
    cliente10.Apellidos = "Ramos Herrera"
    cliente10.CorreoElectronico = "sofia.ramos@email.com"
    cliente10.NumCelular = "+52 449 1234 5678"
    clientes.append(cliente10)

    # 11
    cliente11 = Cliente()
    cliente11.Nombre = "David"
    cliente11.Apellidos = "Navarro Fuentes"
    cliente11.CorreoElectronico = "david.navarro@email.com"
    cliente11.NumCelular = "+52 912 2345 6789"
    clientes.append(cliente11)

    # 12
    cliente12 = Cliente()
    cliente12.Nombre = "Elena"
    cliente12.Apellidos = "Campos Soto"
    cliente12.CorreoElectronico = "elena.campos@email.com"
    cliente12.NumCelular = "+52 777 3456 7890"
    clientes.append(cliente12)

    # 13
    cliente13 = Cliente()
    cliente13.Nombre = "Javier"
    cliente13.Apellidos = "Dominguez Flores"
    cliente13.CorreoElectronico = "javier.dominguez@email.com"
    cliente13.NumCelular = "+52 871 4567 8901"
    clientes.append(cliente13)

    # 14
    cliente14 = Cliente()
    cliente14.Nombre = "Patricia"
    cliente14.Apellidos = "Delgado Vega"
    cliente14.CorreoElectronico = "patricia.delgado@email.com"
    cliente14.NumCelular = "+52 951 5678 9012"
    clientes.append(cliente14)

    # 15
    cliente15 = Cliente()
    cliente15.Nombre = "Roberto"
    cliente15.Apellidos = "Guerrero Robles"
    cliente15.CorreoElectronico = "roberto.guerrero@email.com"
    cliente15.NumCelular = "+52 631 6789 0123"
    clientes.append(cliente15)

    # Insertar todos los clientes
    i = 1
    for cliente in clientes:
        cliente.id = i
        i += 1
        cliente.set_connection(psql_connection)
        cliente.insert()

    # Ejemplares
    ejemplares: List[Ejemplares] = []

    # 1 - Ejemplares de Metamorfosis
    ejemplar1 = Ejemplares()
    ejemplar1.libro = books[0]
    ejemplar1.cantidadExistencia = 5
    ejemplar1.precioVenta = 259.80
    ejemplares.append(ejemplar1)

    # 2 - Ejemplares de El cuento de la criada
    ejemplar2 = Ejemplares()
    ejemplar2.libro = books[1]
    ejemplar2.cantidadExistencia = 8
    ejemplar2.precioVenta = 319.80
    ejemplares.append(ejemplar2)

    # 3 - Ejemplares de Oyasumi Punpun
    ejemplar3 = Ejemplares()
    ejemplar3.libro = books[2]
    ejemplar3.cantidadExistencia = 3
    ejemplar3.precioVenta = 379.80
    ejemplares.append(ejemplar3)

    # 4 - Ejemplares de No tengo boca y debo gritar
    ejemplar4 = Ejemplares()
    ejemplar4.libro = books[3]
    ejemplar4.cantidadExistencia = 6
    ejemplar4.precioVenta = 239.80
    ejemplares.append(ejemplar4)

    # 5 - Ejemplares de 1984
    ejemplar5 = Ejemplares()
    ejemplar5.libro = books[4]
    ejemplar5.cantidadExistencia = 10
    ejemplar5.precioVenta = 279.80
    ejemplares.append(ejemplar5)

    # 6 - Ejemplares de Harry Potter y la Piedra Filosofal
    ejemplar6 = Ejemplares()
    ejemplar6.libro = books[5]
    ejemplar6.cantidadExistencia = 12
    ejemplar6.precioVenta = 299.80
    ejemplares.append(ejemplar6)

    # 7 - Ejemplares de El resplandor
    ejemplar7 = Ejemplares()
    ejemplar7.libro = books[6]
    ejemplar7.cantidadExistencia = 7
    ejemplar7.precioVenta = 339.80
    ejemplares.append(ejemplar7)

    # 8 - Ejemplares de Asesinato en el Oriente Expreso
    ejemplar8 = Ejemplares()
    ejemplar8.libro = books[7]
    ejemplar8.cantidadExistencia = 9
    ejemplar8.precioVenta = 259.80
    ejemplares.append(ejemplar8)

    # 9 - Ejemplares de El Alquimista
    ejemplar9 = Ejemplares()
    ejemplar9.libro = books[8]
    ejemplar9.cantidadExistencia = 11
    ejemplar9.precioVenta = 219.80
    ejemplares.append(ejemplar9)

    # 10 - Ejemplares de Fundación
    ejemplar10 = Ejemplares()
    ejemplar10.libro = books[9]
    ejemplar10.cantidadExistencia = 4
    ejemplar10.precioVenta = 359.80
    ejemplares.append(ejemplar10)

    # 11 - Ejemplares de Frankenstein
    ejemplar11 = Ejemplares()
    ejemplar11.libro = books[10]
    ejemplar11.cantidadExistencia = 6
    ejemplar11.precioVenta = 239.80
    ejemplares.append(ejemplar11)

    # 12 - Ejemplares de Rayuela
    ejemplar12 = Ejemplares()
    ejemplar12.libro = books[11]
    ejemplar12.cantidadExistencia = 3
    ejemplar12.precioVenta = 399.80
    ejemplares.append(ejemplar12)

    # 13 - Ejemplares de Cien años de soledad
    ejemplar13 = Ejemplares()
    ejemplar13.libro = books[12]
    ejemplar13.cantidadExistencia = 8
    ejemplar13.precioVenta = 299.80
    ejemplares.append(ejemplar13)

    # 14 - Ejemplares de El Señor de los Anillos
    ejemplar14 = Ejemplares()
    ejemplar14.libro = books[13]
    ejemplar14.cantidadExistencia = 5
    ejemplar14.precioVenta = 459.80
    ejemplares.append(ejemplar14)

    # 15 - Ejemplares de El retrato de Dorian Gray
    ejemplar15 = Ejemplares()
    ejemplar15.libro = books[14]
    ejemplar15.cantidadExistencia = 7
    ejemplar15.precioVenta = 279.80
    ejemplares.append(ejemplar15)

    # Insertar todos los ejemplares
    for ejemplar in ejemplares:
        ejemplar.set_connection(psql_connection)
        ejemplar.insert()

    # CompraCabecera
    compras_cabecera: List[CompraCabecera] = []

    # 1
    compra1 = CompraCabecera()
    compra1.Fecha = "2026-01-05"
    compra1.Cliente = clientes[0]
    compra1.TotalCompra = 519.60
    compras_cabecera.append(compra1)

    # 2
    compra2 = CompraCabecera()
    compra2.Fecha = "2026-01-10"
    compra2.Cliente = clientes[1]
    compra2.TotalCompra = 639.60
    compras_cabecera.append(compra2)

    # 3
    compra3 = CompraCabecera()
    compra3.Fecha = "2026-01-15"
    compra3.Cliente = clientes[2]
    compra3.TotalCompra = 379.80
    compras_cabecera.append(compra3)

    # 4
    compra4 = CompraCabecera()
    compra4.Fecha = "2026-01-20"
    compra4.Cliente = clientes[3]
    compra4.TotalCompra = 959.40
    compras_cabecera.append(compra4)

    # 5
    compra5 = CompraCabecera()
    compra5.Fecha = "2026-01-25"
    compra5.Cliente = clientes[4]
    compra5.TotalCompra = 279.80
    compras_cabecera.append(compra5)

    # 6
    compra6 = CompraCabecera()
    compra6.Fecha = "2026-02-01"
    compra6.Cliente = clientes[5]
    compra6.TotalCompra = 599.60
    compras_cabecera.append(compra6)

    # 7
    compra7 = CompraCabecera()
    compra7.Fecha = "2026-02-05"
    compra7.Cliente = clientes[6]
    compra7.TotalCompra = 339.80
    compras_cabecera.append(compra7)

    # 8
    compra8 = CompraCabecera()
    compra8.Fecha = "2026-02-10"
    compra8.Cliente = clientes[7]
    compra8.TotalCompra = 779.40
    compras_cabecera.append(compra8)

    # 9
    compra9 = CompraCabecera()
    compra9.Fecha = "2026-02-15"
    compra9.Cliente = clientes[8]
    compra9.TotalCompra = 219.80
    compras_cabecera.append(compra9)

    # 10
    compra10 = CompraCabecera()
    compra10.Fecha = "2026-02-20"
    compra10.Cliente = clientes[9]
    compra10.TotalCompra = 719.60
    compras_cabecera.append(compra10)

    # 11
    compra11 = CompraCabecera()
    compra11.Fecha = "2026-02-25"
    compra11.Cliente = clientes[10]
    compra11.TotalCompra = 479.60
    compras_cabecera.append(compra11)

    # 12
    compra12 = CompraCabecera()
    compra12.Fecha = "2026-03-01"
    compra12.Cliente = clientes[11]
    compra12.TotalCompra = 799.60
    compras_cabecera.append(compra12)

    # 13
    compra13 = CompraCabecera()
    compra13.Fecha = "2026-03-05"
    compra13.Cliente = clientes[12]
    compra13.TotalCompra = 599.60
    compras_cabecera.append(compra13)

    # 14
    compra14 = CompraCabecera()
    compra14.Fecha = "2026-03-10"
    compra14.Cliente = clientes[13]
    compra14.TotalCompra = 919.60
    compras_cabecera.append(compra14)

    # 15
    compra15 = CompraCabecera()
    compra15.Fecha = "2026-03-15"
    compra15.Cliente = clientes[14]
    compra15.TotalCompra = 279.80
    compras_cabecera.append(compra15)

    # Insertar todas las compras cabecera
    i = 1
    for compra in compras_cabecera:
        compra.id = i
        i += 1
        compra.set_connection(psql_connection)
        compra.insert()

    # CompraDetalle
    compra_detalles: List[CompraDetalle] = []

    # 1 - Detalles para compra 1
    detalle1 = CompraDetalle()
    detalle1.CompraCabecera = compras_cabecera[0]
    detalle1.libro = books[0]
    detalle1.Cantidad = 2
    detalle1.Precio = 259.80
    compra_detalles.append(detalle1)

    # 2 - Detalles para compra 2
    detalle2 = CompraDetalle()
    detalle2.CompraCabecera = compras_cabecera[1]
    detalle2.libro = books[1]
    detalle2.Cantidad = 2
    detalle2.Precio = 319.80
    compra_detalles.append(detalle2)

    # 3 - Detalles para compra 3
    detalle3 = CompraDetalle()
    detalle3.CompraCabecera = compras_cabecera[2]
    detalle3.libro = books[2]
    detalle3.Cantidad = 1
    detalle3.Precio = 379.80
    compra_detalles.append(detalle3)

    # 4 - Detalles para compra 4
    detalle4 = CompraDetalle()
    detalle4.CompraCabecera = compras_cabecera[3]
    detalle4.libro = books[3]
    detalle4.Cantidad = 3
    detalle4.Precio = 239.80
    compra_detalles.append(detalle4)

    # 5 - Detalles para compra 5
    detalle5 = CompraDetalle()
    detalle5.CompraCabecera = compras_cabecera[4]
    detalle5.libro = books[4]
    detalle5.Cantidad = 1
    detalle5.Precio = 279.80
    compra_detalles.append(detalle5)

    # 6 - Detalles para compra 6
    detalle6 = CompraDetalle()
    detalle6.CompraCabecera = compras_cabecera[5]
    detalle6.libro = books[5]
    detalle6.Cantidad = 2
    detalle6.Precio = 299.80
    compra_detalles.append(detalle6)

    # 7 - Detalles para compra 7
    detalle7 = CompraDetalle()
    detalle7.CompraCabecera = compras_cabecera[6]
    detalle7.libro = books[6]
    detalle7.Cantidad = 1
    detalle7.Precio = 339.80
    compra_detalles.append(detalle7)

    # 8 - Detalles para compra 8
    detalle8 = CompraDetalle()
    detalle8.CompraCabecera = compras_cabecera[7]
    detalle8.libro = books[7]
    detalle8.Cantidad = 3
    detalle8.Precio = 259.80
    compra_detalles.append(detalle8)

    # 9 - Detalles para compra 9
    detalle9 = CompraDetalle()
    detalle9.CompraCabecera = compras_cabecera[8]
    detalle9.libro = books[8]
    detalle9.Cantidad = 1
    detalle9.Precio = 219.80
    compra_detalles.append(detalle9)

    # 10 - Detalles para compra 10
    detalle10 = CompraDetalle()
    detalle10.CompraCabecera = compras_cabecera[9]
    detalle10.libro = books[9]
    detalle10.Cantidad = 2
    detalle10.Precio = 359.80
    compra_detalles.append(detalle10)

    # 11 - Detalles para compra 11
    detalle11 = CompraDetalle()
    detalle11.CompraCabecera = compras_cabecera[10]
    detalle11.libro = books[10]
    detalle11.Cantidad = 2
    detalle11.Precio = 239.80
    compra_detalles.append(detalle11)

    # 12 - Detalles para compra 12
    detalle12 = CompraDetalle()
    detalle12.CompraCabecera = compras_cabecera[11]
    detalle12.libro = books[11]
    detalle12.Cantidad = 2
    detalle12.Precio = 399.80
    compra_detalles.append(detalle12)

    # 13 - Detalles para compra 13
    detalle13 = CompraDetalle()
    detalle13.CompraCabecera = compras_cabecera[12]
    detalle13.libro = books[12]
    detalle13.Cantidad = 2
    detalle13.Precio = 299.80
    compra_detalles.append(detalle13)

    # 14 - Detalles para compra 14
    detalle14 = CompraDetalle()
    detalle14.CompraCabecera = compras_cabecera[13]
    detalle14.libro = books[13]
    detalle14.Cantidad = 2
    detalle14.Precio = 459.80
    compra_detalles.append(detalle14)

    # 15 - Detalles para compra 15
    detalle15 = CompraDetalle()
    detalle15.CompraCabecera = compras_cabecera[14]
    detalle15.libro = books[14]
    detalle15.Cantidad = 1
    detalle15.Precio = 279.80
    compra_detalles.append(detalle15)

    # Insertar todos los detalles de compra
    for detalle in compra_detalles:
        detalle.set_connection(psql_connection)
        detalle.insert()


if __name__ == "__main__":
    main()
