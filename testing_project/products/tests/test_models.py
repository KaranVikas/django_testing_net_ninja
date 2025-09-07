from django.core.exceptions  import ValidationError
from django.test import TestCase
from products.models import Product

class ProductModelTest(TestCase):
  def setUp(self):
    self.product = Product(name="Test Product", price=100.00, stock_count=10)

  def test_in_stock_property(self):
    self.assertTrue(self.product.in_stock)

    self.product.stock_count = 0
    self.assertFalse(self.product.in_stock)

  def test_get_discounted_price(self):
    self.assertEqual(self.product.get_discounted_price(10), 90.00)
    self.assertEqual(self.product.get_discounted_price(50), 50.00)
    self.assertEqual(self.product.get_discounted_price(10), 90)

  def test_negative_price_validations(self):
    self.product.price = -100.00
    with self.assertRaises(ValidationError):
      self.product.clean()

  def test_negative_stock_count_validations(self):
    self.product.stock_count = -10
    with self.assertRaises(ValidationError):
      self.product.clean()


