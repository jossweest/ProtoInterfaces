import psycopg2


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
