import csv


# first we iterate over values in dictionary
# to get total value of all keys
def display_inventory(inventory):
    
    values = inventory.values()
    inv_total = 0
    for value in values:
        inv_total += value
    # then we "inventory"(dictionary)
    # into "inventory_display"(list) and use "for loop"
    # to iterate over elements and print them
    inventory_display = list(inventory.items())
    print("Inventory:")
    for items, values in inventory_display:
        print(items, values)
    print("Total number of items: %d\n" % inv_total)


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, to_add):
    
    counter = 0
    while counter < len(to_add):
        if to_add[counter] not in inventory:
            inventory[to_add[counter]] = 1
        else:
            for i in inventory:
                if i == to_add[counter]:
                    inventory[i] += 1
            counter += 1
    return(inventory)


# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order='count,asc'):

    headers = '''INVENTORY:\nCOUNT           ITEM NAME
-------------------------'''
    width_1 = 5
    width_2 = 19
    if order is None:
        print(headers)
        for key, value in inventory.items():
            value = str(value)
            print('{} {}'.format((value.rjust(width_1)), (key.rjust(width_2))))
        total_number_of_items = sum(inventory.values())
        print("Total number of items: %d\n-------------------------" %
              total_number_of_items)

    elif order == 'count,desc':
        print(headers)
        for key, value in sorted([(value, key) for (key, value) in inventory.items()], reverse=True):
            key = str(key)
            value = str(value)
            print('{} {}'.format((key.rjust(width_1)), (value.rjust(width_2))))
        total_number_of_items = sum(inventory.values())
        print("Total number of items: %d\n-------------------------" % total_number_of_items)

    elif order == 'count,asc':
        print(headers)
        for key, value in sorted([(value, key) for (key, value) in inventory.items()]):
            key = str(key)
            value = str(value)
            print('{} {}'.format((key.rjust(width_1)), (value.rjust(width_2))))
        total_number_of_items = sum(inventory.values())
        print("Total number of items: %d\n-------------------------" % total_number_of_items)


def import_inventory(inventory, filename="import_inventory.csv"):

    with open(filename, 'r') as filename:
        imported_items = filename.read()
        loot = imported_items.split(',')
        add_to_inventory(inventory, to_add=loot)
    return inventory


def export_inventory(inventory, filename="export_inventory.csv"):

    counter = 0
    keys = list(inventory.keys())
    values = list(inventory.values())
    text = ""
    values_list_lenght = len(values)
    while counter < values_list_lenght:
        text += (keys[counter] + ',') * values[counter]
        counter += 1
    text = text[:-1]
    with open(filename, 'w') as filename:
        filename.write(text)


def main():

    inventory = {'rope': 1, 'torch': 6, 'gold coin': 42,
                 'dagger': 1, 'arrow': 12}
    added_items = ["battleaxe", "spear", "bow", "bow"]
    display_inventory(inventory)
    add_to_inventory(inventory, to_add=added_items)
    print_table(inventory, order='count,desc')
    import_inventory(inventory, "test_inventory.csv")
    print_table(inventory, order='count,asc')
    export_inventory(inventory, "export_invenory.csv")

main()
