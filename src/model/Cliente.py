from dataclasses import dataclass, field
from src.model.Model import Model
from typing import Optional, List, Iterable


# - [] Cliente(IdCliente, Nombre, Apellidos, CorreoElectronico, NumCelular)


@dataclass
class Cliente(Model):
    table: str = "Clientes"
    IdCliente: int = field(default_factory=int)
    Nombre: str = field(default_factory=str)
    Apellidos: str = field(default_factory=str)
    CorreoElectronico: str = field(default_factory=str)
    NumCelular: str = field(default_factory=str)

    @property
    def id(self) -> int:
        return self.IdCliente

    @id.setter
    def id(self, value: int):
        self.IdCliente = value

    def _create_table_query(self) -> str:
        return f"""
        CREATE TABLE IF NOT EXISTS {self.table} (
            IdCliente SERIAL PRIMARY KEY,
            Nombre VARCHAR(255) NOT NULL,
            Apellidos VARCHAR(255) NOT NULL,
            CorreoElectronico VARCHAR(255) NOT NULL,
            NumCelular VARCHAR(20) NOT NULL
        );
        """

    def _insert_query(self) -> str:
        return f"""
        INSERT INTO {self.table} (Nombre, Apellidos, CorreoElectronico, NumCelular)
        VALUES ('{self.Nombre}', '{self.Apellidos}', '{self.CorreoElectronico}', '{self.NumCelular}');
        """

    def _update_query(self) -> str:
        return f"""
        UPDATE {self.table}
        SET Nombre = '{self.Nombre}',
            Apellidos = '{self.Apellidos}',
            CorreoElectronico = '{self.CorreoElectronico}',
            NumCelular = '{self.NumCelular}'
        WHERE IdCliente = {self.IdCliente};
        """

    def _delete_query(self) -> str:
        return f"""
        DELETE FROM {self.table}
        WHERE IdCliente = {self.IdCliente};
        """

    def select(self, columns: Optional[List[str]] = None, where: Optional[str] = None, order_by: Optional[str] = None, limit: Optional[int] = None) -> Iterable[Cliente]:
        query = self._select_query(columns, where, order_by, limit)
        results = self._execute_and_fetch_all(query)

        for result in results:
            yield Cliente(IdCliente=result[0], Nombre=result[1], Apellidos=result[2], CorreoElectronico=result[3], NumCelular=result[4])

    def fetch_by_id(self) -> None:
        result = next(Cliente.select(
            where=f"IdCliente = '{self.IdCliente}'"), None)
        if result is not None:
            self.Nombre = result.Nombre
            self.Apellidos = result.Apellidos
            self.CorreoElectronico = result.CorreoElectronico
            self.NumCelular = result.NumCelular
