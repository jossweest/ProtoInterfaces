from dataclasses import field, dataclass
from src.model.Model import Model
from src.model.Libro import Libro
from src.model.CompraCabecera import CompraCabecera
from typing import Optional, List, Iterable


# - [] CompraDetalle(IdCompra, ISBN, cantidad, precio)

@dataclass
class CompraDetalle(Model):
    table: str = "CompraDetalle"
    compraCabecera: CompraCabecera = field(default_factory=CompraCabecera)
    libro: Libro = field(default_factory=Libro)
    Cantidad: int = field(default_factory=int)
    Precio: float = field(default_factory=float)

    @property
    def id(self) -> int:
        return self.compraCabecera.id

    @id.setter
    def id(self, value: int):
        self.compraCabecera.id = value

    def _create_table_query(self) -> str:
        return f"""
        CREATE TABLE IF NOT EXISTS {self.table} (
            IdCompra INT NOT NULL REFERENCES CompraCabecera(IdCompra),
            ISBN VARCHAR(255) NOT NULL REFERENCES Libro(ISBN),
            Cantidad INT NOT NULL,
            Precio DECIMAL(10, 2) NOT NULL,
            PRIMARY KEY (IdCompra, ISBN)
        );
        """

    def _insert_query(self) -> str:
        return f"""
        INSERT INTO {self.table} (IdCompra, ISBN, Cantidad, Precio)
        VALUES ({self.compraCabecera.id}, '{self.libro.id}', {self.Cantidad}, {self.Precio});
        """

    def _update_query(self) -> str:
        return f"""
        UPDATE {self.table}
        SET Cantidad = {self.Cantidad},
            Precio = {self.Precio}
        WHERE IdCompra = {self.compraCabecera.id}
        AND ISBN = '{self.libro.id}';
        """

    def _delete_query(self) -> str:
        return f"""
        DELETE FROM {self.table}
        WHERE IdCompra = {self.compraCabecera.id}
        AND ISBN = '{self.libro.id}';
        """

    def select(self, columns: Optional[List[str]] = None, where: Optional[str] = None, order_by: Optional[str] = None, limit: Optional[int] = None) -> Iterable[CompraDetalle]:
        query = self._select_query(columns, where, order_by, limit)
        results = self._execute_and_fetch_all(query)

        for result in results:
            yield CompraDetalle(
                compraCabecera=CompraCabecera(IdCompra=result[0]),
                libro=Libro(ISBN=result[1]),
                Cantidad=result[2],
                Precio=result[3]
            )

    def fetch_by_id(self) -> None:
        result = next(CompraDetalle.select(
            where=f"IdCompra = {self.compraCabecera.id} AND ISBN = '{self.libro.id}'"), None)
        if result is not None:
            self.Cantidad = result.Cantidad
            self.Precio = result.Precio
