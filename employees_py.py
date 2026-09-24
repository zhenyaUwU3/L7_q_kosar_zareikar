employees = {
    "E01": {"name": "Ali", "age": 28, "salary": 3000},
    "E02": {"name": "Sara", "age": 32, "salary": 4500},
    "E03": {"name": "Reza", "age": 25, "salary": 2800}
}


def highest_salary(employees):
    highest = 0
    name = ""

    for employee in employees:
        salary = employees[employee]["salary"]

        if salary > highest:
            highest = salary
            name = employees[employee]["name"]

    return name


def lowest_salary(employees):
    lowest = 10000
    name = ""

    for employee in employees:
        salary = employees[employee]["salary"]

        if salary < lowest:
            lowest = salary
            name = employees[employee]["name"]

    return name


def salary_more_than_3000(employees):
    names = []

    for employee in employees:
        if employees[employee]["salary"] > 3000:
            names.append(employees[employee]["name"])

    return names


def salary_more_than(employees, number):
    names = []

    for employee in employees:
        if employees[employee]["salary"] > number:
            names.append(employees[employee]["name"])

    return names


def average_salary(employees):
    total = 0

    for employee in employees:
        total = total + employees[employee]["salary"]

    return total / len(employees)

#2\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
sales = (("Ali", "Laptop", 1200),
    ("Sara", "Phone", 800),
    ("Ali", "Phone", 800),
    ("Reza", "Laptop", 1200),
    ("Sara", "Laptop", 1200),
    ("Ali", "Mouse", 50))


def person_sales(sales):
    result = {}

    for sale in sales:
        name = sale[0]
        price = sale[2]

        if name in result:
            result[name] = result[name] + price
        else:
            result[name] = price

    return result


def product_sales(sales):
    result = {}

    for sale in sales:
        product = sale[1]

        if product in result:
            result[product] = result[product] + 1
        else:
            result[product] = 1

    return result


def total_income(sales):
    total = 0

    for sale in sales:
        total = total + sale[2]

    return total