

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
def add_to_inventory(inventory, added_items):

    counter = 0
    while counter < len(added_items):
        if added_items[counter] not in inventory:
            inventory[added_items[counter]] = 1
        else:
            for i in inventory:
                if i == added_items[counter]:
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
def print_table(inventory, width_1, width_2, headers, order='count,asc'):

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


def main():

    inventory = {'rope': 1, 'torch': 6, 'gold coin': 42,
                 'dagger': 1, 'arrow': 12}
    added_items = ['knife', 'dagger', 'dagger', 'axe']
    headers = '''INVENTORY:\nCOUNT           ITEM NAME
-------------------------'''
    width_1 = 5
    width_2 = 19
    display_inventory(inventory)
    add_to_inventory(inventory, added_items)
    print_table(inventory, width_1, width_2, headers, order='count,desc')
main()
