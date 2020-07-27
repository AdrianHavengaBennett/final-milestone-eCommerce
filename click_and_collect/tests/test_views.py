from django.test import TestCase
from django.urls import reverse


class TestViews(TestCase):
	"""The following tests the views"""

	def test_click_and_collect_GET(self):
		response = self.client.get(reverse('click_and_collect'))

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'click_and_collect/click_and_collect_locations.html')
