from menu_item import MenuItem
from menu_manager import MenuManager

def show_user_menu():
    choice = input("""\n View an Item (V)\n Add an Item (A)\n Delete an Item (D)\n Update an Item (U)\n Show the Menu(S)""")
    
    if  choice == 'v':
        pass
    elif choice == 'a':
        add_item_to_menu()
    elif choice == 'd':
        remove_item_from_menu()
    elif choice == 'u':
        update_item_from_menu()
    elif choice == 's':
        show_restaurant_menu()
    else:
        choice = input("Please a valid choice")


def view_menu_item():
    item = input("Enter which item you would like to view: ")
    menu_item = MenuManager.get_by_name(item)
    return print(menu_item)

def add_item_to_menu():
    new_item_name = input(" enter item_name ")
    new_item_price = input(" enter item_price ")
    item = MenuItem(new_item_name, new_item_price)
    item.save()
    print(f"{new_item_name} was added to menu_items")
    return item

def remove_item_from_menu():
    item_name_remove = input("enter item_name to remove")
    item = MenuItem(item_name_remove)
    item.delete()
    return f"{item.name} was deleted from menu_items"

def update_item_from_menu():
    item_name_update = input("enter item_name to update")
    item_name_new = input("enter item_name to update")
    item_price_new = input("enter item_price to udpate")
    item = MenuItem(item_name_update)
    item.update(item_name_new, item_price_new)
    return f"You update {item_name_update} to {item_name_new}, {item_price_new}"

def show_restaurant_menu():
    menu = MenuManager.get_all()
    return print(menu)

show_user_menu()