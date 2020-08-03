from django.test import SimpleTestCase
from django.urls import reverse, resolve

from products.views import (
    show_products,
    show_product_detail,
    show_category_products,
)


class TestUrls(SimpleTestCase):
    """The following tests the urls"""

    def test_show_products_url_resolves(self):
        url = reverse('products-home')
        self.assertEquals(resolve(url).func, show_products)

    def test_show_product_detail_url_resolves(self):
        url = reverse('product-detail', args=[1])
        self.assertEquals(resolve(url).func, show_product_detail)

    def test_show_category_products_url_resolves(self):
        url = reverse('category-products', args=[1])
        self.assertEquals(resolve(url).func, show_category_products)
