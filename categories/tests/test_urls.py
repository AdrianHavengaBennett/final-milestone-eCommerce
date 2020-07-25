from django.test import SimpleTestCase
from django.urls import reverse, resolve
from categories.views import show_categories


class TestUrls(SimpleTestCase):
	"""The following tests the urls"""

	def test_show_categories_url_resolves(self):
		url = reverse('categories')
		self.assertEquals(resolve(url).func, show_categories)
