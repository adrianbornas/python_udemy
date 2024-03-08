import psycopg2 as db

# Connection data on docker-compose file
connection = db.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='postgres'
)

transaction_error = False

try:
    with connection:
        with connection.cursor() as cursor:
            query1 = 'INSERT INTO person(name, surname, email) VALUES (%s, %s, %s)'
            values1 = ('John', 'Doe', 'john@test.com')
            cursor.execute(query1, values1)

            print(f'Inserted {cursor.rowcount} rows')

            query2 = 'SELECT max(id) FROM person'
            cursor.execute(query2)
            max_id = cursor.fetchone()

            print(f'Actual max id: {max_id}')

            query3 = 'UPDATE person SET name = %s, surname = %s, email = %s WHERE id = %s'
            values3 = ('Jack', 'Sparrow', 'js@test.com', max_id)
            cursor.execute(query3, values3)

            print(f'Updated {cursor.rowcount} rows')

            query4 = 'DELETE FROM person WHERE id = %s'
            values4 = (max_id,)
            cursor.execute(query4, values4)

            print(f'Deleted {cursor.rowcount} rows')
except Exception as e:
    transaction_error = True
    print(f'EXCEPTION: There was an error: {type(e)} - {e}')
    print('ROLLBACK')
finally:
    connection.close()

if not transaction_error:
    print(f'Transaction executed')
