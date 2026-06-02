from typing import List, Optional, Union
from src.model.Model import Model
import psycopg2

from src.model import Model


class AbstractConnection:
    _connection: psycopg2._T_conn

    def connect(self, host: str, database: str, user: str, password: str):
        raise NotImplemented()

    def _execute(self, query):
        cursor = self._connection.cursor()
        cursor.execute(query)
        cursor.close()

    def _execute_and_fetch_one(self, query: str):
        cursor = self._connection.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()

        return result

    def _execute_and_fetch_all(self, query: str):
        cursor = self._connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()

        return results

    def version(self):
        raise NotImplemented()

    def create_table(self, name: str,  *args) -> None:
        raise NotImplemented()

    def insert_table(self, name: str,  values: Union[List, tuple]) -> None:
        raise NotImplemented()

    def select_table(self, name: str, columns: Union[List, tuple], filter: str = "", order: str = "") -> List[Model]:
        raise NotImplemented()

    def update(self, name: str, values: Union[List, tuple], filter: str = "") -> None:
        raise NotImplemented()

    def delete(self, name: str, filter: str = "") -> None:
        raise NotImplemented()
