import csv
import json
import random
from datetime import datetime

USERS = 1000

PURCHASE_QUANTITY = 1000

MIN_PRODUCTS = 5
MAX_PRODUCTS = 30

MIN_ITEMS = 2
MAX_ITEMS = 5

def generate_user_id():
    '''
    generates a random user id in range of USERS
    '''
    return random.randint(1, USERS)

def generate_datetime(min_year = 1990, max_year = 2018):
    year = random.randint(min_year, max_year)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    h = random.randint(0, 23)
    m = random.randint(0, 59)
    s = random.randint(0, 59)

    date = datetime(year, month, day, h, m, s)
    return date.isoformat()

def generate_quantity(a, b):
    '''
    generates a random quantity between the intervals
    '''
    return random.randint(a, b)

def gererate_random_items(products, quantity):
    '''
    generates random products for the purchase
    '''
    # items = [random.choice(products) for _ in range(quantity)]
    items = []
    for _ in range(quantity):
        item = random.choice(products)
        while item['name'] in items:
            item = random.choice(products)
        items.append(item)

    return items

def gererate_random_purchase(items, user_id, date):
    '''
    generates random quantity to each item
    '''
    for item in items:
        quantity = generate_quantity(MIN_ITEMS, MAX_ITEMS)
        item['quantity'] = quantity
        item['date'] = date
        item['user_id'] = user_id

def read_products(filename):
    f = open(filename, 'r')

    if f.mode == 'r':
        content = f.read().split('\n')

    products = []
    for line in content:
        products.append(json.loads(line))
    return products

def write_csv(purchase):
    with open('purchase.csv', 'w') as csvfile:
        field_names = ['user_id', 'date', 'name', 'brand', 'price', 'image', 'quantity']
        writer = csv.DictWriter(csvfile, fieldnames=field_names)

        writer.writeheader()
        writer.writerows(purchase)
        # for i in purchase:
        #     writer.writerow(i)

    csvfile.close()

def main():
    products = read_products('products.json')

    purchase = []
    for _ in range(PURCHASE_QUANTITY):
        products_quantity = generate_quantity(MIN_PRODUCTS, MAX_PRODUCTS)
        items = gererate_random_items(products, products_quantity)
        user_id = generate_user_id()
        date = generate_datetime()
        gererate_random_purchase(items, user_id, date)
        purchase += items

    # print(items)
    write_csv(purchase)



if __name__ == '__main__':
    main()