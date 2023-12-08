import connection
from slugify import slugify


def get_all(name, category):
    conn = connection.connect()
    if not conn:
        return {'type': 'error', 'message': 'Failed to connect to database'}

    try:
        conn_cursor = conn.cursor()

        sql = "SELECT * FROM products WHERE (name LIKE %s OR category LIKE %s OR brand LIKE %s)"
        params = (f'%{name}%', f'%{name}%', f'%{name}%')

        if category:
            sql += " AND category = %s"
            params += (category,)

        conn_cursor.execute(sql, params)
        result = conn_cursor.fetchall()

        products = [{
            'id': x[0],
            'name': x[1],
            'slug': x[2],
            'category': x[3],
            'brand': x[4],
            'price': x[5],
            'images_url': x[6],
        } for x in result]

        return {'type': 'success', 'data': products}
    finally:
        if conn:
            conn_cursor.close()
            conn.close()


def get_all_product_slug(conn, conn_cursor):
    if not conn or not conn_cursor:
        conn = connection.connect()
        if not conn:
            return {'type': 'error', 'message': 'Failed to connect to database'}
        conn_cursor = conn.cursor()

    conn_cursor.execute("SELECT slug FROM products")
    return conn_cursor.fetchall()


def add_list(products):
    if not products:
        return {'type': 'error', 'message': 'No data'}

    conn = connection.connect()
    if not conn:
        return {'type': 'error', 'message': 'Failed to connect to database'}

    try:
        conn_cursor = conn.cursor()

        all_product_slug = [x[0]
                            for x in get_all_product_slug(conn, conn_cursor)]

        sql = "INSERT INTO products (name, slug, category, brand, price, images_url) VALUES (%s, %s, %s, %s, %s, %s)"
        val = []

        for product in products:
            product_slug = slugify(product.name)

            if product_slug not in all_product_slug:
                val.append((product.name, product_slug, product.category,
                            product.brand, product.price, product.images_url))

        if val:
            conn_cursor.executemany(sql, val)
            conn.commit()

        return {'type': 'success', 'message': 'Successfully'}
    finally:
        if conn:
            conn_cursor.close()
            conn.close()


def add(name, category, brand, price, images_url):
    conn = connection.connect()
    if not conn:
        return {'type': 'error', 'message': 'Failed to connect to database'}

    try:
        conn_cursor = conn.cursor()

        all_product_slug = [x[0]
                            for x in get_all_product_slug(conn, conn_cursor)]

        product_slug = slugify(name)
        if product_slug in all_product_slug:
            return {'type': 'error', 'message': 'Product name is already exists'}

        sql = f"INSERT INTO products (name, slug, category, brand, price, images_url) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (name, product_slug, category, brand, price, images_url)

        conn_cursor.execute(sql, val)
        conn.commit()

        return {'type': 'success', 'message': 'Successfully'}
    finally:
        if conn:
            conn_cursor.close()
            conn.close()
