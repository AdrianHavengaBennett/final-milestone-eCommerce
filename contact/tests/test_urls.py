from django.test import SimpleTestCase
from django.urls import reverse, resolve
from contact.views import contact_us, thank_you


class TestUrls(SimpleTestCase):
	"""The following tests the urls"""

	def test_contact_us_url_resolves(self):
		url = reverse('contact-us')
		self.assertEquals(resolve(url).func, contact_us)

	def test_thank_you_url_resolves(self):
		url = reverse('thank-you')
		self.assertEquals(resolve(url).func, thank_you)
