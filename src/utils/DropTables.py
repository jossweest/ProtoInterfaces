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


def main():

    db_config = config(
        file=Path.cwd() / "config.ini",
        section="db"
    )

    psql_connection = PostgresqlConnection()
    psql_connection.connect(**db_config)

    for model_class in [CompraDetalle, Ejemplares, CompraCabecera, Libro, Cliente, Editorial, Autor]:
        model: Model = model_class()
        model.set_connection(psql_connection)
        print(f"Eliminando tabla '{model_class.table}'...")
        model.drop_table()


if __name__ == "__main__":
    main()
