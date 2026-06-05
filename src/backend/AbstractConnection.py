from __future__ import annotations
import psycopg2


class AbstractConnection:
    _connection: psycopg2._T_conn

    def set_connection(self, connection: AbstractConnection):
        self._connection = connection._connection

    def connect(self, host: str, database: str, user: str, password: str):
        raise NotImplemented()

    def _execute(self, query):
        cursor = self._connection.cursor()
        try:
            cursor.execute(query)
            self._connection.commit()
        except psycopg2.Error as e:
            self._connection.rollback()
            raise e
        finally:
            cursor.close()

    def _execute_and_fetch_one(self, query: str):
        cursor = self._connection.cursor()
        try:
            cursor.execute(query)
            results = cursor.fetchone()
        except psycopg2.Error as e:
            self._connection.rollback()
            raise e
        finally:
            cursor.close()

        return results

        return result

    def _execute_and_fetch_all(self, query: str):
        cursor = self._connection.cursor()
        try:
            cursor.execute(query)
            results = cursor.fetchall()
        except psycopg2.Error as e:
            self._connection.rollback()
            raise e
        finally:
            cursor.close()

        return results

    def version(self):
        raise NotImplemented()
