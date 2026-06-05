# Examen práctico: Librería

**UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO**

**Profesora:** Carol Leyva Pelaez

**Materia:** Bases de Datos 1

**Alumnos:**

1. Irma Joseline Garcia Aguirre
2. Gael González Méndez

# Instalación

## Requisitos

- Python 3.8 o superior
- PostgreSQL

## Instalación

Instalar las dependencias Python del proyecto:

```bash
pip install -r requirements.txt
```

## Configurar PostgreSQL

Crear un usuario y una base de datos (ejemplo):

```bash
sudo -u postgres psql -c "CREATE USER pollo_admin WITH PASSWORD 'password';"
sudo -u postgres psql -c "CREATE DATABASE pollo_library OWNER pollo_admin;"
```

Guardar variables en config.ini

```ini
[db]
host=localhost
database=pollo_library
user=pollo_admin
password=password
port=5432

```

## Ejecutar la aplicación

Ejecute la aplicación según la convención del proyecto. Por ejemplo:

```bash
python main.py
```

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
- [ ] Generar dos pantallas para realizar el registro de datos, una pantalla para modificar y los siguientes reportes:
- [ ] Mostrar los datos de los libros incluidos en los pedido de una fecha determinada por el usuario.
- [ ] Indicar el título de todos los libros cuya cantidad en stock sea menor a 5
- [ ] Indicar el nombre de todos los libros registrados con el nombre de autor y editorial.

### Manejo de la base de datos

- [x] Crear la base de datos en el SGBD que haya elegido.
- [x] Insertar 15 registros en cada una de las tablas creadas.
