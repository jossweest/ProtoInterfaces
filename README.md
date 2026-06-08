# Examen práctico: Librería

**UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO**

**Profesora:** Carol Leyva Pelaez  
**Materia:** Bases de Datos 1

**Alumnos:**

1. Irma Joseline Garcia Aguirre
2. Gael González Méndez

---

## Instalación

### Requisitos

- Python 3.8 o superior
- PostgreSQL

### Dependencias

Instala las dependencias del proyecto con:

```bash
pip install -r requirements.txt
```

### Configuración de PostgreSQL

Crea el usuario y la base de datos:

```bash
sudo -u postgres psql -c "CREATE USER pollo_admin WITH PASSWORD 'password';"
sudo -u postgres psql -c "CREATE DATABASE pollo_library OWNER pollo_admin;"
```

Guarda las credenciales en `config.ini`:

```ini
[db]
host=localhost
database=pollo_library
user=pollo_admin
password=password
port=5432
```

> **Nota:** Es posible que PostgreSQL requiera configuración previa para habilitar la autenticación por contraseña.

### Ejecución

```bash
python3 main.pyw
```

---

## Scripts de utilidad

| Comando                             | Descripción                                  |
| ----------------------------------- | -------------------------------------------- |
| `python3 -m src.utils.CreateTables` | Crea las tablas en la base de datos          |
| `python3 -m src.utils.InsertData`   | Inserta los registros precargados            |
| `python3 -m src.utils.DropTables`   | Elimina todas las tablas de la base de datos |

---

## Vistas

### Libro

![Vista: Libro](images/Vista_libro.png)

Pantalla principal para gestionar el catálogo de libros. Permite registrar, consultar, modificar y eliminar libros del sistema.

#### CREATE

Crea la tabla en la base de datos:

```sql
CREATE TABLE IF NOT EXISTS libro (
ISBN VARCHAR(255) PRIMARY KEY,
Titulo VARCHAR(255) NOT NULL,
IdEditorial INT NOT NULL REFERENCES Editoriales(idEditorial),
IdAutor INT NOT NULL REFERENCES Autores(idAutor),
Ubicacion VARCHAR(255) NOT NULL
);
```

Inserta un nuevo libro:

```sql
INSERT INTO {table} (ISBN, Titulo, IdEditorial, IdAutor, Ubicacion)
VALUES ('{ISBN}', '{Titulo}', '{Editorial.id}', '{selAutor.id}', '{Ubicación}');
```

#### READ

La consulta de selección se genera automáticamente a través del método `_select_query` de la clase `Model`. Selecciona todos los registros de la tabla, con soporte opcional para filtros, ordenamiento y límite de resultados:

```python
# src.model.Model.py
def _select_query(
        self,
        columns: Optional[List[str]] = None,
        where: Optional[str] = None,
        order_by: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> str:
        """Genera el SQL para seleccionar registros de la tabla"""
        column_list = "*" if not columns else ", ".join(columns)
        query = f"SELECT {column_list} FROM {table}"

        if where:
            query += f" WHERE {where}"
        if order_by:
            query += f" ORDER BY {order_by}"
        if limit is not None:
            query += f" LIMIT {limit}"

        return f"{query};"
```

#### UPDATE

Actualiza los datos de un libro existente, identificado por su ISBN:

```sql
UPDATE {table}
SET Titulo = '{Titulo}',
IdEditorial = '{Editorial.id}',
IdAutor = '{Autor.id}',
Ubicacion = '{Ubicación}'
WHERE ISBN = '{ISBN}';
```

#### DELETE

Elimina un libro de la tabla por su ISBN:

```sql
DELETE FROM {table}
WHERE ISBN = '{ISBN}';
```

---

### Autor

![Vista: Autor](images/Vista_autor.png)

Pantalla para gestionar el catálogo de autores registrados en el sistema.

#### CREATE

Crea la tabla en la base de datos:

```sql
CREATE TABLE IF NOT EXISTS {table} (
    idAutor SERIAL PRIMARY KEY,
    Nombre VARCHAR(255) NOT NULL
);
```

Inserta un nuevo autor:

```sql
INSERT INTO {table} (Nombre)
VALUES ('{Nombre}');
```

#### READ

Al igual que en la vista de Libro, la consulta se genera dinámicamente a través de `_select_query`. Selecciona todos los autores registrados en la tabla:

```python
# src.model.Model.py
def _select_query(
        self,
        columns: Optional[List[str]] = None,
        where: Optional[str] = None,
        order_by: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> str:
        """Genera el SQL para seleccionar registros de la tabla"""
        column_list = "*" if not columns else ", ".join(columns)
        query = f"SELECT {column_list} FROM {table}"

        if where:
            query += f" WHERE {where}"
        if order_by:
            query += f" ORDER BY {order_by}"
        if limit is not None:
            query += f" LIMIT {limit}"

        return f"{query};"
```

#### UPDATE

Actualiza el nombre de un autor existente, identificado por su ID:

```sql
UPDATE {table}
SET Nombre = '{Nombre}'
WHERE idAutor = {idAutor};
```

#### DELETE

Elimina un autor de la tabla por su ID:

```sql
DELETE FROM {table}
WHERE idAutor = {idAutor};
```

---

## Reportes

### Pedidos por fecha

![Vista de reporte: Libros solicitados en determinada fecha](images/Reporte_pedidos_por_fecha.png)

Muestra todos los libros incluidos en los pedidos de una fecha específica, junto con su cantidad, precio y fecha de compra.

```sql
SELECT
l.isbn, l.titulo, cd.cantidad, cd.precio, cc.fecha
FROM compradetalle cd
JOIN compracabecera cc ON cd.idcompra = cc.idcompra
JOIN libro l ON cd.isbn = l.isbn
WHERE cc.fecha = '{fecha}'
ORDER BY cc.fecha, l.titulo;
```

---

### Libros con stock menor a 5

![Vista de reporte: Libros con stock menor a 5](images/Reporte_stock_menor_a_5.png)

Lista todos los libros cuya cantidad en existencia es inferior a 5 unidades, ordenados de menor a mayor stock.

```sql
SELECT  l.isbn, l.titulo, e.cantidadexistencia AS stock, l.ubicacion
FROM libro l
JOIN ejemplares e ON l.isbn = e.isbn
WHERE e.cantidadexistencia < 5
ORDER BY e.cantidadexistencia;
```

---

### Libros registrados por autor y editorial

![Vista de reporte: Libros, autor y editorial](images/Reporte_libros_autor_editorial.png)

Muestra el catálogo completo de libros con el nombre de su autor y editorial correspondiente, ordenados alfabéticamente por título.

```sql
SELECT l.isbn, l.titulo, a.nombre AS autor, e.nombre AS editorial, l.ubicacion
FROM libro l
JOIN autores a ON l.idautor = a.idautor
JOIN editoriales e ON l.ideditorial = e.ideditorial
ORDER BY l.titulo;
```

---

## Rúbrica de evaluación

### Base de datos

- [x] Libro(ISBN, Titulo, IdEditorial, IdAutor, Ubicacion)
- [x] Editorial(IdEditorial, nombre)
- [x] Autor(IdAutor, Nombre)
- [x] Ejemplares(ISBN, cantidadExistencia, precioVenta)
- [x] CompraCabecera(IdCompra, Fecha, IdCliente, TotalCompra)
- [x] CompraDetalle(IdCompra, ISBN, cantidad, precio)
- [x] Cliente(IdCliente, Nombre, Apellidos, CorreoElectronico, NumCelular)

### Interfaz gráfica

- [x] De acuerdo al lenguaje programación de su elección, generar la conexión a la base de datos.
- [x] Generar dos pantallas para realizar el registro de datos, una pantalla para modificar y los siguientes reportes:
- [x] Mostrar los datos de los libros incluidos en los pedido de una fecha determinada por el usuario.
- [x] Indicar el título de todos los libros cuya cantidad en stock sea menor a 5
- [x] Indicar el nombre de todos los libros registrados con el nombre de autor y editorial.

### Manejo de la base de datos

- [x] Crear la base de datos en el SGBD que haya elegido.
- [x] Insertar 15 registros en cada una de las tablas creadas.
