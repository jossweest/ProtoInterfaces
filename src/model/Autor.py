from dataclasses import field
from src.model.Model import Model
from __future__ import annotations
from typing import Optional, Iterable

# - [] Autor(IdAutor, Nombre)


class Autor(Model):
    table: str = "Autores"
    idAutor: str = field(default_factory=str)
    Nombre: str = field(default_factory=str)

    @property
    def id(self) -> str:
        return self.idAutor

    @id.setter
    def id(self, value: str):
        self.idAutor = value

    def _create_table_query(self) -> str:
        return f"""
        CREATE TABLE IF NOT EXISTS {self.table} (
            idAutor VARCHAR(255) PRIMARY KEY,
            Nombre VARCHAR(255) NOT NULL
        );
        """

    def _insert_query(self) -> str:
        return f"""
        INSERT INTO {self.table} (idAutor, Nombre)
        VALUES ('{self.idAutor}', '{self.Nombre}');
        """

    def _update_query(self) -> str:
        return f"""
        UPDATE {self.table}
        SET Nombre = '{self.Nombre}'
        WHERE idAutor = '{self.idAutor}';
        """

    def _delete_query(self) -> str:
        return f"""
        DELETE FROM {self.table}
        WHERE idAutor = '{self.idAutor}';
        """

    @classmethod
    def select(cls, columns: Optional[Iterable[str]] = None, where: Optional[str] = None, order_by: Optional[str] = None, limit: Optional[int] = None) -> Iterable[Autor]:
        query = cls._select_query(columns, where, order_by, limit)
        results = cls._execute_and_fetch_all(query)

        for result in results:
            yield cls(idAutor=result[0], Nombre=result[1])

    def fetch_by_id(self) -> None:
        result = next(Autor.select(
            where=f"idAutor = '{self.idAutor}'"), None)
        if result is not None:
            self.Nombre = result.Nombre
