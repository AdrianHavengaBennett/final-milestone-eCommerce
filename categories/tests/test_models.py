from django.test import TestCase

from categories.models import Category


class TestCategoryModel(TestCase):
    """The following tests the Category model"""

    def test_category_string_method_returns_category_name(self):
        category = Category.objects.create(category_name='Test Category')

        self.assertEqual(category.__str__(), category.category_name)
