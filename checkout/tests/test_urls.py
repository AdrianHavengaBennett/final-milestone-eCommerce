from django.test import SimpleTestCase
from django.urls import reverse, resolve
from checkout.views import checkout, checkout_success, get_location_info


class TestUrls(SimpleTestCase):
	"""The following tests the urls"""

	def test_checkout_url_resolves(self):
		url = reverse('checkout')
		self.assertEquals(resolve(url).func, checkout)

	def test_checkout_success_url_resolves(self):
		url = reverse('checkout-success', args=[1])
		self.assertEquals(resolve(url).func, checkout_success)

	def test_get_location_info_url_resolves(self):
		url = reverse('get-location-info')
		self.assertEquals(resolve(url).func, get_location_info)
