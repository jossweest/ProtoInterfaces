from __future__ import annotations
from dataclasses import field, dataclass
from src.model.Model import Model
from typing import Optional, Iterable

# - [] Autor(IdAutor, Nombre)


@dataclass
class Autor(Model):
    table: str = "Autores"
    idAutor: int = field(default_factory=int)
    Nombre: str = field(default_factory=str)

    @property
    def id(self) -> int:
        return self.idAutor

    @id.setter
    def id(self, value: int):
        self.idAutor = value

    def _create_table_query(self) -> str:
        return f"""
        CREATE TABLE IF NOT EXISTS {self.table} (
            idAutor SERIAL PRIMARY KEY,
            Nombre VARCHAR(255) NOT NULL
        );
        """

    def _insert_query(self) -> str:
        return f"""
        INSERT INTO {self.table} (Nombre)
        VALUES ('{self.Nombre}');
        """

    def _update_query(self) -> str:
        return f"""
        UPDATE {self.table}
        SET Nombre = '{self.Nombre}'
        WHERE idAutor = {self.idAutor};
        """

    def _delete_query(self) -> str:
        return f"""
        DELETE FROM {self.table}
        WHERE idAutor = {self.idAutor};
        """

    def select(self, columns: Optional[Iterable[str]] = None, where: Optional[str] = None, order_by: Optional[str] = None, limit: Optional[int] = None) -> Iterable[Autor]:
        query = self._select_query(columns, where, order_by, limit)
        results = self._execute_and_fetch_all(query)

        for result in results:
            yield Autor(idAutor=result[0], Nombre=result[1])

    def fetch_by_id(self) -> None:
        result = next(Autor.select(
            where=f"idAutor = '{self.idAutor}'"), None)
        if result is not None:
            self.Nombre = result.Nombre
