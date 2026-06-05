from dataclasses import field, dataclass
from src.model.Model import Model
from src.model.Cliente import Cliente
from typing import Optional, List, Iterable


# - [] CompraCabecera(IdCompra, Fecha, IdCliente, TotalCompra)

@dataclass
class CompraCabecera(Model):
    table: str = "CompraCabecera"
    IdCompra: int = field(default_factory=int)
    Fecha: str = field(default_factory=str)
    Cliente: Cliente = field(default_factory=Cliente)
    TotalCompra: float = field(default_factory=float)

    @property
    def id(self) -> int:
        return self.IdCompra

    @id.setter
    def id(self, value: int):
        self.IdCompra = value

    def _create_table_query(self) -> str:
        return f"""
        CREATE TABLE IF NOT EXISTS {self.table} (
            IdCompra SERIAL PRIMARY KEY,
            Fecha DATE NOT NULL,
            IdCliente INT NOT NULL REFERENCES Clientes(IdCliente),
            TotalCompra DECIMAL(10, 2) NOT NULL
        );
        """

    def _insert_query(self) -> str:
        return f"""
        INSERT INTO {self.table} (Fecha, IdCliente, TotalCompra)
        VALUES ('{self.Fecha}', '{self.Cliente.id}', {self.TotalCompra});
        """

    def _update_query(self) -> str:
        return f"""
        UPDATE {self.table}
        SET Fecha = '{self.Fecha}',
            IdCliente = '{self.Cliente.id}',
            TotalCompra = {self.TotalCompra}
        WHERE IdCompra = {self.IdCompra};
        """

    def _delete_query(self) -> str:
        return f"""
        DELETE FROM {self.table}
        WHERE IdCompra = {self.IdCompra};
        """

    def select(self, columns: Optional[List[str]] = None, where: Optional[str] = None, order_by: Optional[str] = None, limit: Optional[int] = None) -> Iterable[CompraCabecera]:
        query = self._select_query(columns, where, order_by, limit)
        results = self._execute_and_fetch_all(query)

        for result in results:
            yield self(
                IdCompra=result[0],
                Fecha=result[1],
                Cliente=Cliente(IdCliente=result[2]),
                TotalCompra=result[3]
            )

    def fetch_by_id(self) -> None:
        result = next(CompraCabecera.select(
            where=f"IdCompra = {self.IdCompra}"), None)
        if result is not None:
            self.Fecha = result.Fecha
            self.Cliente = result.Cliente
            self.TotalCompra = result.TotalCompra
