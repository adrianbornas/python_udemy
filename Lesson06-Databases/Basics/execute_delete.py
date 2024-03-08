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
            query = 'DELETE FROM person WHERE id = %s'
            person_id = input('Id to delete: ')
            values = (person_id,)
            cursor.execute(query, values)

            # For multiple deletes:
            # query = 'DELETE FROM person WHERE id IN %s'
            # values = (id1, id2, id3)
            # cursor.execute(query, values)

            deleted = cursor.rowcount
            print(f'Deleted rows: {deleted}')
except Exception as e:
    print(f'EXCEPTION: There was an error: {type(e)} - {e}')
finally:
    connection.close()
