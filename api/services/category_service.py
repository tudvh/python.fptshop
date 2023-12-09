import connection


def get_all():
    conn = connection.connect()
    if not conn:
        return {'type': 'error', 'message': 'Failed to connect to database'}

    try:
        conn_cursor = conn.cursor()
        conn_cursor.execute('SELECT distinct category FROM products')
        return [x[0] for x in conn_cursor.fetchall()]
    finally:
        if conn:
            conn_cursor.close()
            conn.close()
