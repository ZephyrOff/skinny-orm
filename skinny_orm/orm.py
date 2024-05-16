from skinny_orm.sqlite_orm import SqliteOrm
import sqlite3


class Orm:
    def __new__(cls, connection, create_tables_if_not_exists=True, parse_fields=True, connection_type="sqlite3"):
        if isinstance(connection, str):
            if connection_type=="sqlite3":
                connection = sqlite3.connect(connection)


        if 'sqlite3' in str(connection.__class__):
            return SqliteOrm(connection, create_tables_if_not_exists, parse_fields)
        else:
            raise NotImplementedError
