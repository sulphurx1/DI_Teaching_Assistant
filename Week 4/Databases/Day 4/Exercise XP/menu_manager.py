import psycopg2

connection=psycopg2.connect(
    database= 'restaurant',
    user='postgres',
    password='test',
    host='localhost',
    port='5432'
)

cursor = connection.cursor()

class MenuManager():


    @classmethod
    def get_by_name(cls, get_item):
        query = f"""SELECT item_name, item_price FROM menu_items WHERE item_name = '{get_item}' """
        cursor.execute(query)
        result = cursor.fetchall
        if result == None:
            print(f"No such item {get_item} in menu list")

        else: 
            return result
        
    
    @classmethod
    def get_all(cls):
        query = """SELECT item_name, item_price FROM menu_items"""
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    

cursor.close()
connection.close()


