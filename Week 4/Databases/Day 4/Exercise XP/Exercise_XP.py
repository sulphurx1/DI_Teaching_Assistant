      import psycopg2

connection = psycopg2.connect(
    database = 'restaurant',
    user = 'postgres',
    password = 'root',
    host = 'localhost',
    port = '5432'
)

cursor = connection.cursor()

class MenuItem:
    def __init__(self, name, price = 0):
        self.name = name
        self.price = price

    def save(self):
        query = f"""INSERT INTO menu_items (item_name, item_price) VALUES ('{self.name}', '{self.price}')"""
        cursor.execute(query)
        connection.commit()

    def delete(self):
        query = f"""DELETE FROM menu_items WHERE item_name = '{self.name}' """
        cursor.execute(query)
        connection.commit()

    def update(self, new_name, new_price):
        query = f"""UPDATE menu_items SET item_name = '{new_name}', item_price ='{new_price}' WHERE item_name = '{self.name}' """
        cursor.execute(query)
        connection.commit()

cursor.close()
connection.close()