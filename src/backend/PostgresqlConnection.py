import psycopg2
from src.backend.AbstractConnection import AbstractConnection


class PostgresqlConnection(AbstractConnection):

    def connect(self, host: str, database: str, user: str, password: str):
        self._connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )

    def version(self):
        return self._execute_and_fetch_one("SELECT version();")

    def create_table(self, name: str,  *args) -> None:
        query = f"CREATE TABLE {name} ({args.join(', ')});"
        self._execute(query)
