stuff = {'gold coin': 42, 'rope':1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def display_inventory(inventory):
    print('Inventory: ')
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
    print("Total number of items: " + str(item_total))




