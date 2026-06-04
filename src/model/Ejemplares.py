from dataclasses import dataclass, field
from src.model.Model import Model
from src.model.Libro import Libro
from typing import Optional, List, Iterable


# - [] Ejemplares(ISBN, cantidadExistencia, precioVenta)


@dataclass
class Ejemplares(Model):
    table: str = "Ejemplares"
    libro: Libro = field(default_factory=Libro)
    cantidadExistencia: int = field(default_factory=int)
    precioVenta: float = field(default_factory=float)

    @property
    def id(self) -> str:
        return self.libro.id

    @id.setter
    def id(self, value: str):
        self.libro.id = value

    def _create_table_query(self) -> str:
        return f"""
        CREATE TABLE IF NOT EXISTS {self.table} (
            ISBN VARCHAR(255) PRIMARY KEY REFERENCES Libro(ISBN),
            cantidadExistencia INT NOT NULL,
            precioVenta DECIMAL(10, 2) NOT NULL
        );
        """

    def _insert_query(self) -> str:
        return f"""
        INSERT INTO {self.table} (ISBN, cantidadExistencia, precioVenta)
        VALUES ('{self.libro.id}', {self.cantidadExistencia}, {self.precioVenta});
        """

    def _update_query(self) -> str:
        return f"""
        UPDATE {self.table}
        SET cantidadExistencia = {self.cantidadExistencia},
            precioVenta = {self.precioVenta}
        WHERE ISBN = '{self.libro.id}';
        """

    def _delete_query(self) -> str:
        return f"""
        DELETE FROM {self.table}
        WHERE ISBN = '{self.libro.id}';
        """

    def select(self, columns: Optional[List[str]] = None, where: Optional[str] = None, order_by: Optional[str] = None, limit: Optional[int] = None) -> Iterable[Ejemplares]:
        query = self._select_query(columns, where, order_by, limit)
        results = self._execute_and_fetch_all(query)

        for result in results:
            yield self(
                libro=Libro(ISBN=result[0]),
                cantidadExistencia=result[1],
                precioVenta=result[2]
            )

    def fetch_by_id(self) -> None:
        result = next(Ejemplares.select(
            where=f"ISBN = '{self.libro.id}'"), None)
        if result is not None:
            self.cantidadExistencia = result.cantidadExistencia
            self.precioVenta = result.precioVenta
