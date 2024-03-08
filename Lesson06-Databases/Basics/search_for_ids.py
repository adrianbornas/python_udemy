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
            query = 'SELECT * FROM person WHERE id IN %s'

            ids = input('Person ids (1,2,3,4): ')
            params = (tuple(ids.split(',')),)

            cursor.execute(query, params)
            results = cursor.fetchall()

            for result in results:
                print(result)
except Exception as e:
    print(f'EXCEPTION: There was an error: {type(e)} - {e}')
finally:
    connection.close()
