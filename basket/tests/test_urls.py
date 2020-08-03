from django.test import SimpleTestCase
from django.urls import reverse, resolve

from basket.views import (
    show_basket,
    add_to_basket,
    update_basket,
    remove_from_basket
)


class TestUrls(SimpleTestCase):
    """The following tests the urls"""

    def test_show_basket_url_resolves(self):
        url = reverse('basket')
        self.assertEquals(resolve(url).func, show_basket)

    def test_add_to_basket_url_resolves(self):
        url = reverse('add-to-basket', args=[1])
        self.assertEquals(resolve(url).func, add_to_basket)

    def test_update_basket_url_resolves(self):
        url = reverse('update-basket', args=[1])
        self.assertEquals(resolve(url).func, update_basket)

    def test_remove_from_basket_url_resolves(self):
        url = reverse('remove-item', args=[1])
        self.assertEquals(resolve(url).func, remove_from_basket)
