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
            query = 'UPDATE person SET name = %s, surname = %s, email = %s WHERE id = %s'
            values = ('Jane', 'Doe', 'jane@test.com', 3)
            cursor.execute(query, values)

            # For multiple updates:
            # values = (
            #   ('name1', 'surname1', 'email1', id1),
            #   ('name2', 'surname2', 'email2', id2),
            #   ('name3', 'surname3', 'email3', id3)
            # )
            # cursor.executemany(query, values)

            updated = cursor.rowcount
            print(f'Updated rows: {updated}')
except Exception as e:
    print(f'EXCEPTION: There was an error: {type(e)} - {e}')
finally:
    connection.close()
