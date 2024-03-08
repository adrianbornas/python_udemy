import sys

from psycopg2 import pool

from DataAccess.constants import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME
from logger_base import log


class ConnectionDB:
    """
    Manages database connection
    """
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def _obtain_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CON,
                    cls._MAX_CON,
                    user=DB_USER,
                    password=DB_PASS,
                    host=DB_HOST,
                    port=DB_PORT,
                    database=DB_NAME
                )

                log.debug(f'Pool obtained: {cls._pool}'.center(30, '-'))
            except Exception as e:
                log.error(f'ERROR {type(e)} - {e}')
                sys.exit()
        return cls._pool

    @classmethod
    def obtain_connection(cls):
        connection = cls._obtain_pool().getconn()
        log.debug(f'Connection obtained: {connection}'.center(30, '-'))
        return connection

    @classmethod
    def free_connection(cls, connection):
        cls._obtain_pool().putconn(connection)
        log.debug(f'Free connection: {connection}'.center(30, '-'))

    @classmethod
    def close_connections(cls):
        cls._obtain_pool().closeall()
        log.debug(f'Pool closed'.center(30, '-'))


if __name__ == '__main__':
    # Get connections
    connection1 = ConnectionDB.obtain_connection()
    connection2 = ConnectionDB.obtain_connection()

    # Free connection
    ConnectionDB.free_connection(connection1)

    # Get connection
    connection1 = ConnectionDB.obtain_connection()

