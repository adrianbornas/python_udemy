# DATABASE CONSTANTS
DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASS = 'admin'
DB_HOST = '127.0.0.1'
DB_PORT = '5432'

# QUERY CONSTANTS
SELECT_PERSON = 'SELECT * FROM person'
INSERT_PERSON = 'INSERT INTO person(name, surname, email) VALUES (%s, %s, %s)'
UPDATE_PERSON = 'UPDATE person SET name = %s, surname = %s, email = %s WHERE id = %s'
DELETE_PERSON = 'DELETE FROM person WHERE id = %s'
