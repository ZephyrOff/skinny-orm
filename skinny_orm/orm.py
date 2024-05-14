from skinny_orm.sqlite_orm import SqliteOrm
import sqlite3


class Orm:
    def __new__(self, connection, create_tables_if_not_exists=True, parse_fields=True, connection_type="sqlite3"):
        if isinstance(connection, str):
            if connection_type=="sqlite3":
                self.connection = sqlite3.connect(connection)
        else:
            self.connection = connection


        if 'sqlite3' in str(self.connection.__class__):
            return SqliteOrm(self.connection, create_tables_if_not_exists, parse_fields)
        else:
            raise NotImplementedError


    def __enter__(self):
        return self


    def __exit__(self, *args):
        self.connection.close()
