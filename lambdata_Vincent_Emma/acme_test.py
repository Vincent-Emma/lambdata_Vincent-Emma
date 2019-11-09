#!/usr/bin/env python
import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS

class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)


    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)


    def test_stealabilityt(self):
        """Test stealability with default product values."""
        prod = Product('Test Product')
        self.assertMultiLineEqual(prod.stealability(), 'Kinda stealable.')
        

if __name__ == '__main__':
    unittest.main()