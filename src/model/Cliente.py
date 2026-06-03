from dataclasses import field
from src.model.Model import Model
from typing import Optional, List, Iterable


# - [] Cliente(IdCliente, Nombre, Apellidos, CorreoElectronico, NumCelular)


class Cliente(Model):
    table: str = "Clientes"
    IdCliente: str = field(default_factory=str)
    Nombre: str = field(default_factory=str)
    Apellidos: str = field(default_factory=str)
    CorreoElectronico: str = field(default_factory=str)
    NumCelular: str = field(default_factory=str)

    @property
    def id(self) -> str:
        return self.IdCliente

    @id.setter
    def id(self, value: str):
        self.IdCliente = value

    def _create_table_query(self) -> str:
        return f"""
        CREATE TABLE IF NOT EXISTS {self.table} (
            IdCliente VARCHAR(255) PRIMARY KEY,
            Nombre VARCHAR(255) NOT NULL,
            Apellidos VARCHAR(255) NOT NULL,
            CorreoElectronico VARCHAR(255) NOT NULL,
            NumCelular VARCHAR(20) NOT NULL
        );
        """

    def _insert_query(self) -> str:
        return f"""
        INSERT INTO {self.table} (IdCliente, Nombre, Apellidos, CorreoElectronico, NumCelular)
        VALUES ('{self.IdCliente}', '{self.Nombre}', '{self.Apellidos}', '{self.CorreoElectronico}', '{self.NumCelular}');
        """

    def _update_query(self) -> str:
        return f"""
        UPDATE {self.table}
        SET Nombre = '{self.Nombre}',
            Apellidos = '{self.Apellidos}',
            CorreoElectronico = '{self.CorreoElectronico}',
            NumCelular = '{self.NumCelular}'
        WHERE IdCliente = '{self.IdCliente}';
        """

    def _delete_query(self) -> str:
        return f"""
        DELETE FROM {self.table}
        WHERE IdCliente = '{self.IdCliente}';
        """

    @classmethod
    def select(cls, columns: Optional[List[str]] = None, where: Optional[str] = None, order_by: Optional[str] = None, limit: Optional[int] = None) -> Iterable[Cliente]:
        query = cls._select_query(columns, where, order_by, limit)
        results = cls._execute_and_fetch_all(query)

        for result in results:
            yield cls(IdCliente=result[0], Nombre=result[1], Apellidos=result[2], CorreoElectronico=result[3], NumCelular=result[4])

    def fetch_by_id(self) -> None:
        result = next(Cliente.select(
            where=f"IdCliente = '{self.IdCliente}'"), None)
        if result is not None:
            self.Nombre = result.Nombre
            self.Apellidos = result.Apellidos
            self.CorreoElectronico = result.CorreoElectronico
            self.NumCelular = result.NumCelular
