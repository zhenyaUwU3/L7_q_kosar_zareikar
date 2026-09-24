products = {
    "laptop": 1200,
    "phone": 800,
    "tablet": 500,
    "headphone": 150,
    "mouse": 50
}


def max_price(products):
    max_price = 0

    for price in products.values():
        if price > max_price:
            max_price = price

    return max_price


def max_product(products):
    max_price = 0
    product_name = ""

    for product in products:
        if products[product] > max_price:
            max_price = products[product]
            product_name = product

    return product_name


def min_price(products):
    min_price = 1200

    for price in products.values():
        if price < min_price:
            min_price = price

    return min_price


def min_product(products):
    min_price = 1200
    product_name = ""

    for product in products:
        if products[product] < min_price:
            min_price = products[product]
            product_name = product

    return product_name


def total_price(products):
    total = 0

    for price in products.values():
        total = total + price

    return total


def average_price(products):
    total = 0

    for price in products.values():
        total = total + price

    return total / len(products)