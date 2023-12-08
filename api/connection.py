import mysql.connector
import time


def connect(trying=30):
    while trying:
        try:
            conn = mysql.connector.connect(
                host="mysql_service",
                port="3306",
                user="root",
                password="psw123",
                database="8_db"
            )
            return conn
        except mysql.connector.Error as err:
            print(f'Error connecting to database: {err}')
            print(
                f'Retrying in 1 second... (remaining attempts: {trying - 1})')
            time.sleep(1)
            trying -= 1

    print('Unable to connect to database after multiple attempts.')
    return None
