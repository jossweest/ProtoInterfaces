from dataclasses import field
from src.model.Model import Model
from src.model.Editorial import Editorial
from src.model.Autor import Autor
from typing import Optional, List, Iterable


# - [] Libro(ISBN, Titulo, IdEditorial, IdAutor, Ubicacion)


class Libro(Model):
    table: str = "Libro"
    ISBN: str = field(default_factory=str)
    Titulo: str = field(default_factory=str)
    Editorial: Editorial = field(default_factory=Editorial)
    Autor: Autor = field(default_factory=Autor)
    Ubicación: str = field(default_factory=str)

    @property
    def id(self) -> str:
        return self.ISBN

    @id.setter
    def id(self, value: str):
        self.ISBN = value

    def _create_table_query(self) -> str:
        return f"""
        CREATE TABLE IF NOT EXISTS {self.table} (
            ISBN VARCHAR(255) PRIMARY KEY,
            Titulo VARCHAR(255) NOT NULL,
            IdEditorial INT NOT NULL REFERENCES Editoriales(idEditorial),
            IdAutor INT NOT NULL REFERENCES Autores(idAutor),
            Ubicacion VARCHAR(255) NOT NULL
        );
        """

    def _insert_query(self) -> str:
        return f"""
        INSERT INTO {self.table} (ISBN, Titulo, IdEditorial, IdAutor, Ubicacion)
        VALUES ('{self.ISBN}', '{self.Titulo}', '{self.Editorial.id}', '{self.Autor.id}', '{self.Ubicación}');
        """

    def _update_query(self) -> str:
        return f"""
        UPDATE {self.table}
        SET Titulo = '{self.Titulo}',
            IdEditorial = '{self.Editorial.id}',
            IdAutor = '{self.Autor.id}',
            Ubicacion = '{self.Ubicación}'
        WHERE ISBN = '{self.ISBN}';
        """

    def _delete_query(self) -> str:
        return f"""
        DELETE FROM {self.table}
        WHERE ISBN = '{self.ISBN}';
        """

    def select(self, columns: Optional[List[str]] = None, where: Optional[str] = None, order_by: Optional[str] = None, limit: Optional[int] = None) -> Iterable[Libro]:
        query = self._select_query(columns, where, order_by, limit)
        results = self._execute_and_fetch_all(query)

        for result in results:
            yield self(
                ISBN=result[0],
                Titulo=result[1],
                Editorial=Editorial(idEditorial=result[2]),
                Autor=Autor(idAutor=result[3]),
                Ubicación=result[4]
            )

    def fetch_by_id(self) -> None:
        result = next(Libro.select(where=f"ISBN = '{self.ISBN}'"), None)
        if result is not None:
            self.Titulo = result.Titulo
            self.Editorial = result.Editorial
            self.Autor = result.Autor
            self.Ubicación = result.Ubicación
