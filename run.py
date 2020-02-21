import os
import datetime
import pymysql

username = os.getenv('C9_USER')

connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    with connection.cursor() as cursor:
        # cursor.execute("DELETE FROM Friends WHERE name in ('Bob', 'Jim')
        connection.commit()
finally:
    connection.close()
