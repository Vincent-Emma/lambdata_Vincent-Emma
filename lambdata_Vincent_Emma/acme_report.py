#!/usr/bin/env python
from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', 'Computer']


def generate_products(num_products=30) -> list:
    """Generates a list of 30 products"""
    products = []
    for i in range(num_products):
        prod = Product(f'{ADJECTIVES[randint(0,4)]} {NOUNS[randint(0,4)]}')
        prod.weight = randint(5,100)
        prod.price = randint(5,100)
        prod.flammability = uniform(0.0,2.5)
        products.append(prod)
    return products


def _build_report_metrics(products):
    """Builds unique_names count, average_price, average_weight, average_flam to send to
    the inventory report function"""
    unique_names = len(set([i.name for i in products]))
    average_price = sum([i.price for i in products]) / len(products)
    average_weight = sum([i.weight for i in products]) / len(products)
    average_flam = sum([i.flammability for i in products]) / len(products)

    return unique_names, average_price, average_weight, average_flam


def inventory_report(products: list) -> str:
    """Gives a detailed report on created products"""
    unique_names, average_price, average_weight, average_flam = _build_report_metrics(products)

    report = f'''ACME CORPORATION OFFICIAL INVENTORY REPORT
    Unique product names: {unique_names}
    Average price: {average_price}
    Average weight: {average_weight}
    Average flammability: {average_flam}'''
    
    return print(report)


if __name__ == '__main__':

    inventory_report(generate_products())