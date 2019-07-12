import random
from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num_products=30):
    products = []
    # TODO - your code! Generate and add random products.
    for _ in range(num_products):
          products.append(Product(sample(ADJECTIVES, 1)[0] + ' ' + sample(NOUNS, 1)[0]))
          products[_].price = int(random.uniform(5,100))
          products[_].weight = int(random.uniform(5,100))
          products[_].flammability = random.uniform(0.0,2.5)
    return products


products = generate_products()
"""
for product in products:
    print(product.flammability)
"""

def inventory_report(products):
    # TODO - your code! Loop over the products to calculate the report.
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    unique = set(products)
    unique_product_names = len(list(unique))
    price=0
    weight=0
    flammability=0
    for product in products:
        price += product.price
        weight+= product.weight
        flammability += product.flammability
    avg_price = price/len(products)
    avg_weight = weight/len(products)
    avg_flammability = flammability/len(products)
    print('Unique product names: ' + str(unique_product_names))
    print('Average price: ' + str(avg_price))
    print('Average weight: ' + str(avg_weight))
    print('Average flammability: ' + str(avg_flammability))

#inventory_report(products)

if __name__ == '__main__':
    inventory_report(generate_products())
