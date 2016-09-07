# menus will be list, show completed, add, complete
# menu will be
# R- List required items
# C- List completed items
# A- Add new item
# M- Mark an item completed
# Q- Quit

def main():
    menu_options = ["r","c","a","m","q"]
    print("Welcome to Shopping list by Janrich van Heerden")
    print("items loaded from items")
    print("Menu:\nR - List required items\nC - List completed items\n A - add new item\nM - Mark an item completed\n Q - Quit")
    menu_choice=str(input("").lower())
    while menu_choice in menu_options:
        if menu_choice == "r":
            #list required items
        elif menu_choice == "c":
            #list completed items
        elif menu_choice == "a":
            #add new item
        elif menu_choice == "m":
            #list required items
def menu(menu_choice,menu_options):
    while menu_choice not in menu_options:
        menu_choice=str(input("Please enter a valid input, r,c,a,m,q"))
    return menu_choice

def required_items():

def list_data():

def completed_items():

def add_new_item():

def mark_complete():

def compile_new_list():