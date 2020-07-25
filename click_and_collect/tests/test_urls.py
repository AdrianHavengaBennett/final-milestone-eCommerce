from django.test import SimpleTestCase
from django.urls import reverse, resolve
from click_and_collect.views import click_and_collect, get_location


class TestUrls(SimpleTestCase):
	"""The following tests the urls"""

	def test_click_and_collect_url_resolves(self):
		url = reverse('click_and_collect')
		self.assertEquals(resolve(url).func, click_and_collect)

	def test_get_location_url_resolves(self):
		url = reverse('get-location', args=['keyword'])
		self.assertEquals(resolve(url).func, get_location)
