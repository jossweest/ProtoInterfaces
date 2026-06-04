import psycopg2
from src.backend.AbstractConnection import AbstractConnection


class PostgresqlConnection(AbstractConnection):

    def connect(self, host: str, database: str, user: str, password: str, port: int = 5432):
        self._connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )

    def version(self):
        return self._execute_and_fetch_one("SELECT version();")
