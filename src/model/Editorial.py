from dataclasses import field
from src.model.Model import Model
from typing import Optional, Iterable


# - [] Editorial(IdEditorial, nombre)


class Editorial(Model):
    table: str = "Editoriales"
    idEditorial: str = field(default_factory=str)
    Nombre: str = field(default_factory=str)

    @property
    def id(self) -> str:
        return self.idEditorial

    @id.setter
    def id(self, value: str):
        self.idEditorial = value

    def _create_table_query(self) -> str:
        return f"""
        CREATE TABLE IF NOT EXISTS {self.table} (
            idEditorial VARCHAR(255) PRIMARY KEY,
            Nombre VARCHAR(255) NOT NULL
        );
        """

    def _insert_query(self) -> str:
        return f"""
        INSERT INTO {self.table} (idEditorial, Nombre)
        VALUES ('{self.idEditorial}', '{self.Nombre}');
        """

    def _update_query(self) -> str:
        return f"""
        UPDATE {self.table}
        SET Nombre = '{self.Nombre}'
        WHERE idEditorial = '{self.idEditorial}';
        """

    def _delete_query(self) -> str:
        return f"""
        DELETE FROM {self.table}
        WHERE idEditorial = '{self.idEditorial}';
        """

    @classmethod
    def select(cls, columns: Optional[List[str]] = None, where: Optional[str] = None, order_by: Optional[str] = None, limit: Optional[int] = None) -> Iterable[Editorial]:
        query = cls._select_query(columns, where, order_by, limit)
        results = cls._execute_and_fetch_all(query)

        for result in results:
            yield cls(idEditorial=result[0], Nombre=result[1])

    def fetch_by_id(self) -> None:
        result = next(Editorial.select(
            where=f"idEditorial = '{self.idEditorial}'"), None)
        if result is not None:
            self.Nombre = result.Nombre
