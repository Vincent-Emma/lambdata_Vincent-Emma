#!/usr/bin/env python
import unittest
from random import randint
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme reports are the tops!"""


    def test_default_num_products(self):
        """Test num of product created is 30."""
        prods = generate_products()
        self.assertEqual(len(prods), 30)


    def test_legal_names(self):
        """Test legal names in product creation"""
        prods = generate_products()
        name = prods[randint(0,30)].name
        noun = name.split(' ')[1]
        adj = name.split(' ')[0]
        self.assertIn(noun, NOUNS)
        self.assertIn(adj, ADJECTIVES)


if __name__ == '__main__':
    unittest.main()