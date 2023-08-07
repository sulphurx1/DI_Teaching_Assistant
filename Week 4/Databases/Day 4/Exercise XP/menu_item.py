import  psycopg2

DATABASE = 'restaurant'
PASSWORD = 'test'
USER = 'postgres'
HOST = 'localhost'
PORT = '5432'

connection = psycopg2.connect(
    database = DATABASE,
    user = USER,
    password = PASSWORD,
    host = HOST,
    port = PORT
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


def main():
    item = MenuItem('Burger', 35)
    item.save()
    item.delete()
    item.update('Veggie Burger', 37)

if __name__ == '__main__':
    main()

