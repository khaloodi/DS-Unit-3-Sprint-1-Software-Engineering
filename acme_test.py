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

    def test_price_is_int(self):
        prod = Product('Test Product')
        self.assertTrue(isinstance(prod.price, int))

    def test_flammability_is_float(self):
        prod = Product('Test Product')
        self.assertTrue(isinstance(prod.flammability, float))


if __name__ == '__main__':
    unittest.main()
