import psycopg2 as db

# Connection data on docker-compose file
connection = db.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='postgres'
)

cursor = connection.cursor()
query = 'SELECT * FROM person'
cursor.execute(query)
results = cursor.fetchall()

print(results)

cursor.close()
connection.close()
