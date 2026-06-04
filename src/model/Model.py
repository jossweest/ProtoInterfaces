from dataclasses import dataclass, field
from typing import Any, List, Optional, Iterable
from src.backend.PostgresqlConnection import PostgresqlConnection


@dataclass
class Model(PostgresqlConnection):

    @property
    def fields(self) -> List[str]:
        return [field.name for field in self.__dataclass_fields__.values() if not field.name in ["id"]]

    def create_table(self) -> None:
        """Crea la tabla en la base de datos"""
        query = self._create_table_query()
        self._execute(query)

    def insert(self) -> None:
        """Inserta el registro actual en la base de datos"""
        query = self._insert_query()
        self._execute(query)

    def update(self) -> None:
        """Actualiza el registro actual en la base de datos"""
        query = self._update_query()
        self._execute(query)

    def delete(self) -> None:
        """Elimina el registro actual de la base de datos"""
        query = self._delete_query()
        self._execute(query)

    def _create_table_query(self) -> str:
        """Genera el SQL para crear la tabla"""
        raise NotImplementedError(
            "Subclasses must implement create_table method"
        )

    def _insert_query(self) -> str:
        """Genera el SQL para insertar el registro actual"""
        raise NotImplementedError(
            "Subclasses must implement insert method"
        )

    def select(self, columns: Optional[List[str]] = None, where: Optional[str] = None, order_by: Optional[str] = None, limit: Optional[int] = None) -> Iterable[Any]:
        raise NotImplementedError(
            "Subclasses must implement select method"
        )

    def _update_query(self) -> str:
        """Genera el SQL para actualizar el registro actual"""
        raise NotImplementedError(
            "Subclasses must implement update method"
        )

    def _delete_query(self) -> str:
        """Genera el SQL para eliminar el registro actual"""
        raise NotImplementedError(
            "Subclasses must implement delete method"
        )

    def drop_table(self) -> None:
        """Elimina la tabla de la base de datos"""
        query = f"DROP TABLE IF EXISTS {self.table} CASCADE;"
        self._execute(query)

    def _select_query(
        self,
        columns: Optional[List[str]] = None,
        where: Optional[str] = None,
        order_by: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> str:
        """Genera el SQL para seleccionar registros de la tabla"""
        column_list = "*" if not columns else ", ".join(columns)
        query = f"SELECT {column_list} FROM {self.table}"

        if where:
            query += f" WHERE {where}"
        if order_by:
            query += f" ORDER BY {order_by}"
        if limit is not None:
            query += f" LIMIT {limit}"

        return f"{query};"
