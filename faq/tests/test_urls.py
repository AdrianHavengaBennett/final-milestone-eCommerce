from django.test import SimpleTestCase
from django.urls import reverse, resolve
from faq.views import show_faqs


class TestUrls(SimpleTestCase):
	"""The following tests the urls"""

	def test_show_faqs_url_resolves(self):
		url = reverse('faqs-home')
		self.assertEquals(resolve(url).func, show_faqs)
