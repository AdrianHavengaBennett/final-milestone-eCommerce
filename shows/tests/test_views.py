from django.test import TestCase
from django.urls import reverse


class TestViews(TestCase):
	"""The following tests the views"""

	def test_get_shows_GET(self):
		response = self.client.get(reverse('get-shows'))

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'shows/shows.html')
