import json

class MenuManager:
    def __init__(self):
        self.file = file
        self.menu = menu

        file = 'restaurant_menu.json'
        with open(file, 'r') as f:
            menu = json.load(f)

    def add_item(self, name, price):
        self.menu.append(name, price)

    def remove_item(name):
        



    def save_to_file():
        with open(file, 'w') as f:
            json.dump(self.menu, f)