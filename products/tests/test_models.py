from django.test import TestCase
from products.models import Product
from categories.models import Category


class TestProductModel(TestCase):
	"""The following tests the Product model"""

	def test_product_string_method_returns_product_name(self):
		
		category = Category.objects.create(
			category_name='Testing',
		)

		product = Product.objects.create(
			name='Test Product',
			description='Test Product Description',
			category_name=category,
			price=10.00,
		)
		
		self.assertEqual(product.__str__(), product.name)
