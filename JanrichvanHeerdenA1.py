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
    print("Menu:\nR - List required items\nC - List completed items\nA - add new item\nM - Mark an item completed\nQ - Quit")
    menu_choice=str(input(">>> ").lower())
    while menu_choice in menu_options:
        if menu_choice == "r":
            print("r is good")
            #list required items
        elif menu_choice == "c":
            print("c is good")
            #list completed items
        elif menu_choice == "a":
            print("a is good")
            #add new item
        elif menu_choice == "m":
            print("m is good")
            #list required items
            menu_choice = menu(menu_choice,menu_options)

def menu(menu_choice,menu_options):
    while menu_choice not in menu_options:
        menu_choice=str(input("Please enter a valid input, r,c,a,m,q"))
    return menu_choice

#def required_items():
#
#def list_data():
#
#def completed_items():
#
#def add_new_item():
#
#def mark_complete():
#
#def compile_new_list():
main()