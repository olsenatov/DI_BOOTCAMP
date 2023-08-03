from menu_manager import MenuManager
from menu_item import MenuItem

def show_user_menu():
    print("//Program Menu\\")
    print("View an Item (V)")
    print("Add an Item (A)")
    print("Delete an Item (D)")
    print("Update an Item (U)")
    print("Show the Menu (S)")
    print("Quit (Q)")
    print("//><\\")

def view_item():
    item_name = input("Enter the name of the item you want to view: ")
    item = MenuManager.get_by_name(item_name)
    if item:
        print(f"Item: {item.name}, Price: {item.price}")
    else:
        print(f"Item '{item_name}' not found!")

def add_item_to_menu():
    item_name = input("Enter the name of the new item: ")
    item_price = input("Enter the price of the new item: ")

    try:
        item_price = int(item_price)
        item = MenuItem(item_name, item_price)
        item.save()
        print(f"Item '{item_name}' was added successfully!")
    except ValueError:
        print("Invalid price! Price must be an integer.")

def remove_item_from_menu():
    item_name = input("Enter the name of the item you want to remove from the menu: ")

    item = MenuItem(item_name, 0)  

    try:
        item.delete()
        print(f"Item '{item_name}' was deleted successfully!")
    except:
        print(f"An error occurred while deleting item '{item_name}'.")


def update_item_from_menu():
    item_name = input("Enter the name of the item you want to update: ")
    item_price = input("Enter the price of the item you want to update: ")

    new_item_name = input("Enter the new name for the item: ")
    new_item_price = input("Enter the new price for the item: ")

    item = MenuItem(item_name, int(item_price))

    try:
        new_item_price = int(new_item_price)
        item.update(new_item_name, new_item_price)
        print("Item updated successfully!")
    except ValueError:
        print("Invalid price! Price must be an integer.")
    except:
        print(f"An error occurred while updating item '{item_name}'.")

def show_restaurant_menu():
    menu_items = MenuManager.all_items()
    if menu_items:
        print("//Restaurant Menu\\")
        for item in menu_items:
            print(f"Item: {item.name}, Price: {item.price}")
        print("//><\\")
    else:
        print("The restaurant menu is empty.")

def main():
    while True:
        show_user_menu()
        choice = input("Enter your choice: ").upper()

        if choice == "V":
            view_item()
        elif choice == "A":
            add_item_to_menu()
        elif choice == "D":
            remove_item_from_menu()
        elif choice == "U":
            update_item_from_menu()
        elif choice == "S":
            show_user_menu()
        elif choice == "Q":
            print("Restaurant Menu before exit:")
            show_restaurant_menu()
            print("End of the programm")
            break
        else:
            print("Invalid choice. Please try again.")



main()
