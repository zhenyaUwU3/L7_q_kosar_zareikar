def check_products(inventory):

    available = []
    unavailable = []

    for product in inventory:

        if inventory[product] > 0:
            available.append(product)

        else:
            unavailable.append(product)

    return available, unavailable


inventory = {
    "apple": 20,
    "banana": 5,
    "orange": 0,
    "milk": 12,
    "bread": 0
}

available, unavailable = check_products(inventory)

print(available)
print(unavailable)