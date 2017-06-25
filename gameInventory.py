import csv

from collections import Counter
from tabulate import tabulate

def display_inventory(inventory):
    print("\nInventory: \n")
    for k, v in inventory.items():
        print("%s %s" % (v, k))
    sumofinv = sum(inv.values())
    print("\nTotal number of items: %s" % sumofinv)

def add_to_inventory(inventory, added_items):
    inv_to_count = Counter(inventory)
    added_to_count = Counter(added_items)
    newinv = inv_to_count + added_to_count
    return dict(newinv)

def print_table(inventory, order = ''):
    print("\nInventory: ")
    headers = ['count ', 'item name']
    if order == '':
        data = [(v,k) for k,v in inventory.items()]
    elif order == 'count,asc':
        data = sorted([(v,k) for k,v in inventory.items()])
    elif order == 'count,desc':
        data = sorted([(v,k) for k,v in inventory.items()], reverse = True)
    print(tabulate(data, headers=headers, stralign='right'))
    sumofinv = sum(inv.values())
    print("\nTotal number of items: %s \n" % sumofinv)

def import_inventory(inventory, filename = '/home/peter/CodeCool/import_inventory.csv'):
    with open(filename, 'r', encoding='UTF-8') as f:
        reader = csv.reader(f)
        import_list = list(reader)
        inv_to_count = Counter(inventory)
        import_to_count = Counter(import_list[0])
        add_import = inv_to_count + import_to_count
        return dict(add_import)

def export_inventory(inventory, filename = '/home/peter/CodeCool/export_inventory.csv'):
    with open(filename, 'w') as f:
        [f.write('{0},{1}\n'.format(key, value)) for key, value in inventory.items()]


inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

display_inventory(inv)

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = add_to_inventory(inv, dragon_loot)

display_inventory(inv)

print_table(inv)

inv = import_inventory(inv)

print_table(inv, 'count,desc')

export_inventory(inv)
