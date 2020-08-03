from django.test import SimpleTestCase
from django.urls import reverse, resolve

from search.views import (
    blog_search,
    products_search,
    faqs_search,
    shows_search,
)


class TestUrls(SimpleTestCase):
    """The following tests the urls"""

    def test_blog_search_url_resolves(self):
        url = reverse('blog-search')
        self.assertEquals(resolve(url).func, blog_search)

    def test_products_search_url_resolves(self):
        url = reverse('products-search')
        self.assertEquals(resolve(url).func, products_search)

    def test_faqs_search_url_resolves(self):
        url = reverse('faqs-search')
        self.assertEquals(resolve(url).func, faqs_search)

    def test_shows_search_url_resolves(self):
        url = reverse('shows-search')
        self.assertEquals(resolve(url).func, shows_search)
