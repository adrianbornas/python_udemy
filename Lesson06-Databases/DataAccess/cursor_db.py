from DataAccess.connection_db import ConnectionDB
from logger_base import log


class CursorDB:
    def __init__(self):
        self._connection = None
        self._cursor = None

    def __enter__(self):
        log.debug('__enter__')
        self._connection = ConnectionDB.obtain_connection()
        self._cursor = self._connection.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        log.debug('__exit__')
        if exc_val:
            self._connection.rollback()
            log.error(f'EXCEPTION: {exc_type} {exc_val}: {exc_tb}')
            log.error('ROLLBACK')
        else:
            self._connection.commit()
            log.debug('COMMIT')
        self._cursor.close()
        ConnectionDB.free_connection(self._connection)


if __name__ == '__main__':
    with CursorDB() as cursor:
        log.debug('Inside Cursor\'s with block')
        cursor.execute('SELECT * FROM person')
        log.debug(cursor.fetchall())
