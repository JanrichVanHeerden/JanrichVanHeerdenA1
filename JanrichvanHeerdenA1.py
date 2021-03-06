# menus will be list, show completed, add, complete
# menu will be
# R- List required items
# C- List completed items
# A- Add new item
# M- Mark an item completed
# Q- Quit


def main():
    item_file = open("items.csv", "r")
    menu_options = ["r", "c", "a", "m"]
    total_items_list = []   # just found out split lists wrong, something to do with attributes, thanks trevor
    item_name_list, price_list, priority_list, required_or_completed_list = add_data_to_list(
        item_file)
    item_file.close()
    total_items_list.append(item_name_list)
    total_items_list.append(price_list)
    total_items_list.append(priority_list)
    total_items_list.append(required_or_completed_list)
    print("Welcome to Shopping list by Janrich van Heerden")
    print("{} items loaded from items.csv".format(len(total_items_list[0])))
    print(total_items_list[0])
    print(total_items_list[1])
    print(total_items_list[2])
    print(total_items_list[3])
    print(
        "Menu:\nR - List required items\nC - List completed items\nA - add new item\nM - Mark an item completed\nQ - Quit")
    menu_choice = menu(menu_options)
    while menu_choice in menu_options and menu_choice != "q":
        if menu_choice == "r":
            required_items(total_items_list)
        elif menu_choice == "c":
            completed_items(total_items_list)
        elif menu_choice == "a":
            add_new_item(total_items_list)
        elif menu_choice == "m":
            required_items(total_items_list)
            mark_complete(total_items_list)
        print(
            "Menu:\nR - List required items\nC - List completed items\nA - add new item\nM - Mark an item completed\nQ - Quit")
        menu_choice = menu(menu_options)
    save_to_list(total_items_list)



def menu(menu_options):
    menu_choice = str(input(">>> ").lower())
    while menu_choice not in menu_options and menu_choice != "q":
        menu_choice = str(input(
            "Invalid Menu Choice\nMenu:\nR - List required items\nC - List completed items\nA - add new item\nM - Mark an item completed\nQ - Quit"))
    return menu_choice


def required_items(
        total_items_list):  # how do i sort so it prints on item priority while dynamically changing the item number
    price = 0
    number_of_items = 0
    for product in total_items_list[1]:
        if total_items_list[3][number_of_items] == "r":
            print("{}. {:<20s}$  {:<6.2f}({})".format(number_of_items, total_items_list[0][number_of_items],
                                                      total_items_list[1][number_of_items],
                                                      total_items_list[2][number_of_items]))
            price += total_items_list[1][number_of_items]
        number_of_items += 1
    print("Total expected price for {} items: ${}".format(number_of_items, price))
    return number_of_items


def add_data_to_list(
        item_file):  # splitting the lists. This fucntion incorrectly splits the lists into parallel lists. In hindsight this seemed correct as splitting the code later to add the prices seemed redundent
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
    for product in total_items_list[1]:
        if total_items_list[3][number_of_items] == "c":
            print("{}. {:<20s}$  {:<6.2f}({})".format(number_of_items, total_items_list[0][number_of_items],
                                                      total_items_list[1][number_of_items],
                                                      total_items_list[2][number_of_items]))
            c_in_list = True
            print("Total expected price for {} items: ${}".format(number_of_items, price))
            price += total_items_list[1][number_of_items]
        number_of_items += 1
    if c_in_list == False:  # better way to do this?
        print("No Completed Items")


def add_new_item(total_items_list):
    item_name = str(input("Item name: "))
    item_price = float(input("Item price:$ "))
    item_priority = int(input("Item priority: "))
    required_or_completed = "r"
    print("{}, ${} (priority {}) added to shopping list.".format(item_name, item_price, item_priority))
    total_items_list[0].append(item_name)
    total_items_list[1].append(item_price)
    total_items_list[2].append(item_priority)
    total_items_list[3].append(required_or_completed)


def mark_complete(total_items_list):
    print("Enter the number of an item to mark complete")
    mark_item_complete = int(input(">>>"))
    total_items_list[3][mark_item_complete] = "c"
    print("{} marked as complete.".format(total_items_list[0][mark_item_complete]))


def save_to_list(total_items_list): #open to file as write only then writing to it
    item_file = open("items.csv", "w")
    number_of_items = 0
    for lines in total_items_list[0]:
        print("{},{},{},{}".format(total_items_list[0][number_of_items], total_items_list[1][number_of_items],
                                   total_items_list[2][number_of_items], total_items_list[3][number_of_items]),
              file=item_file)
        number_of_items += 1
    print("{} items saved to items.csv".format(len(total_items_list[0])))


main()
