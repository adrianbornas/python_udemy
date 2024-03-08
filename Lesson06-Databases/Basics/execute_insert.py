import psycopg2 as db

# Connection data on docker-compose file
connection = db.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='postgres'
)

try:
    with connection:
        with connection.cursor() as cursor:
            query = 'INSERT INTO person(name, surname, email) VALUES (%s, %s, %s)'
            name = input('Name: ')
            surname = input('Surname: ')
            email = input('Email: ')

            values = (name, surname, email)
            cursor.execute(query, values)

            # For multiple inserts:
            # values = (
            #   ('name1', 'surname1', 'email1'),
            #   ('name2', 'surname2', 'email2'),
            #   ('name3', 'surname3', 'email3')
            # )
            # cursor.executemany(query, values)

            # ONLY necessary when the connection is manually handled, with context manager it is committed automatically
            # connection.commit()
            # If error occurs, executes rollback automatically

            inserted = cursor.rowcount
            print(f'Inserted rows: {inserted}')
except Exception as e:
    print(f'EXCEPTION: There was an error: {type(e)} - {e}')
finally:
    connection.close()
