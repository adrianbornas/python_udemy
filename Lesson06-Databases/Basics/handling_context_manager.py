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
            query = 'SELECT * FROM person WHERE id = %s'
            id_person = input('Person id: ')
            cursor.execute(query, (id_person,))
            result = cursor.fetchone()
            print(result)
except Exception as e:
    print(f'EXCEPTION: There was an error: {type(e)} - {e}')
finally:
    connection.close()
