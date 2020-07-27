from django.test import TestCase
from django.urls import reverse


class TestViews(TestCase):
	"""The following tests the views"""

	def test_show_faqs_GET(self):
		response = self.client.get(reverse('faqs-home'))

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'faq/faq.html')
