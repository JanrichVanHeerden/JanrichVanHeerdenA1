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
    #print(total_items_list[3])
    #print(total_items_list[0])
    #print(total_items_list[1])
    #print(total_items_list[2])
    print(
        "Menu:\nR - List required items\nC - List completed items\nA - add new item\nM - Mark an item completed\nQ - Quit")
    menu_choice = menu(menu_options)
    while menu_choice in menu_options:
        if menu_choice == "r":
            required_items(total_items_list)
        elif menu_choice == "c":
            completed_items(total_items_list)
        elif menu_choice == "a":
            print("a is good")
            # add new item
        elif menu_choice == "m":
            mark_complete(total_items_list)
        elif menu_choice == "q":
            sys.exit()  # not sure if this is the right way to exit instead of using Break?
        print(
            "Menu:\nR - List required items\nC - List completed items\nA - add new item\nM - Mark an item completed\nQ - Quit")
        menu_choice = menu(menu_options)
    item_file.close()




def menu(menu_options):
    menu_choice = str(input(">>> ").lower())
    while menu_choice not in menu_options:
        menu_choice = str(input("Please enter a valid input, r,c,a,m,q"))
    return menu_choice


def required_items(total_items_list):
    price = 0
    number_of_items = 0
    for product in total_items_list[1]:
        if total_items_list[3][number_of_items] == "r":
            print("{}. {}----{}-----{}".format(number_of_items,total_items_list[0][number_of_items], total_items_list[1][number_of_items], total_items_list[3][number_of_items]))
            price += total_items_list[1][number_of_items]
        number_of_items += 1
    print("Total expected price for {} items: ${}".format(number_of_items,price))
    return number_of_items
    #HOW THE F**K DO I EXIT THIS LIST





def add_data_to_list(item_file):  # this function should allow any data added to be added to the item file
    item_name_list = []
    price_list = []
    priority_list = []
    required_or_completed_list = []
    for line in item_file:
        item_name, item_price, item_priority, required_or_completed = line.split(",")
        item_price = float(item_price)
        required_or_completed = required_or_completed[-4:-1]  # thanks to michael for showing me this formatting trick
        item_name_list.append(item_name)
        priority_list.append(item_priority)
        price_list.append(item_price)
        required_or_completed_list.append(required_or_completed)
    return item_name_list, price_list, priority_list, required_or_completed_list


def completed_items(total_items_list):
    c_in_list = False
    price = 0
    number_of_items = 0
    for product in total_items_list[1]:  # thing what variable is appropriate, we need the item
        if total_items_list[3][number_of_items] == "c":
            print("{}----{}-----{}".format(number_of_items,total_items_list[0][number_of_items], total_items_list[1][number_of_items],
                                           total_items_list[3][number_of_items]))
            c_in_list = True
            print("Total expected price for {} items: ${}".format(number_of_items, price))
            price += total_items_list[1][number_of_items]
        number_of_items += 1
    if c_in_list == False:  #better way to do this?
        print("No Completed Items")



#def add_new_item(item_file):


def mark_complete(total_items_list):
    print("Enter the number of an item to mark complete")  #remove this it doesnt work
    mark_item_complete = str(input(">>>"))

# mark complete =  ask for item number,





main()
