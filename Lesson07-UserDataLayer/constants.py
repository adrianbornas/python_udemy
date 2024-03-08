# DATABASE CONSTANTS
DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASS = 'admin'
DB_HOST = '127.0.0.1'
DB_PORT = '5432'

# QUERY CONSTANTS
SELECT_USER = 'SELECT * FROM custom_user ORDER BY id_user'
INSERT_USER = 'INSERT INTO custom_user(username, password) VALUES (%s, %s)'
UPDATE_USER = 'UPDATE custom_user SET username = %s, password = %s WHERE id_user = %s'
DELETE_USER = 'DELETE FROM custom_user WHERE id_user = %s'
