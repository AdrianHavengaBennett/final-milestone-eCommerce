from django.test import SimpleTestCase
from django.urls import reverse, resolve

from shows.views import get_shows, show_details


class TestUrls(SimpleTestCase):
    """The following tests the urls"""

    def test_get_shows_url_resolves(self):
        url = reverse('get-shows')
        self.assertEquals(resolve(url).func, get_shows)

    def test_show_details_url_resolves(self):
        url = reverse('show-details', args=[1])
        self.assertEquals(resolve(url).func, show_details)
