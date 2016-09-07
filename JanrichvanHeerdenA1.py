# menus will be list, show completed, add, complete
# menu will be
# R- List required items
# C- List completed items
# A- Add new item
# M- Mark an item completed
# Q- Quit
import sys


def main():
    item_file = open("items.csv", "r")
    menu_options = ["r", "c", "a", "m", "q"]
    total_items_list = []
    item_name_list, price_list, priority_list, required_or_completed_list = add_data_to_list(item_file)
    total_items_list.append(item_name_list)
    total_items_list.append(price_list)
    total_items_list.append(priority_list)
    total_items_list.append(required_or_completed_list)
    print("Welcome to Shopping list by Janrich van Heerden")
    print("{} items loaded from items.csv".format(len(total_items_list)))
    print(total_items_list[3])
    print(total_items_list[0])
    print(total_items_list[1])
    print(total_items_list[2])
    print(
        "Menu:\nR - List required items\nC - List completed items\nA - add new item\nM - Mark an item completed\nQ - Quit")
    menu_choice = menu(menu_options)
    while menu_choice in menu_options:
        if menu_choice == "r":
            print("r is good")
            # list required items
        elif menu_choice == "c":
            print("c is good")
            # list completed items
        elif menu_choice == "a":
            print("a is good")
            # add new item
        elif menu_choice == "m":
            print("m is good")
            # list required items
        elif menu_choice == "q":
            sys.exit()  # not sure if this is the right way to exit instead of using Break?
    item_file.close()


def menu(menu_options):
    menu_choice = str(input(">>> ").lower())
    while menu_choice not in menu_options:
        menu_choice = str(input("Please enter a valid input, r,c,a,m,q"))
    return menu_choice


def required_items(total_items_list):
    price = 0
    number_of_items = 0
    for product in total_items_list:  # thing what variable is appropriate, we need the item
        if total_items_list[3][number_of_items] == "r":
            print("{}{}{}".format(total_items_list[0], total_items_list[2], total_items_list[3]))
        number_of_items = +1
        price = +total_items_list[1]
    print("Total expected price for {} items: ${}".format(number_of_items,price))



def add_data_to_list(item_file):  # this function should allow any data added to be added to the item file
    item_name_list = []
    price_list = []
    priority_list = []
    required_or_completed_list = []
    for line in item_file:
        item_name, item_price, item_priority, required_or_completed = line.split(",")
        required_or_completed = required_or_completed[-4:-1]  # thanks to michael for showing me this formatting trick
        item_name_list.append(item_name)
        priority_list.append(item_priority)
        price_list.append(item_price)
        required_or_completed_list.append(required_or_completed)
    return item_name_list, price_list, priority_list, required_or_completed_list


# def completed_items(total_items_list):
#    pass
#    for thing in total_items_list:

# def add_new_item(item_file):
#    pass
# def mark_complete():
#
# def compile_new_list():
main()
