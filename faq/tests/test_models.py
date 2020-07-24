from django.test import TestCase
from faq.models import FAQ


class TestFAQModel(TestCase):
	"""The following tests the FAQ model"""

	def test_question_string_method_returns_the_question(self):
		question = FAQ.objects.create(
			question='Are we testing?',
			answer='A-Firm!',
		)
		
		self.assertEqual(question.__str__(), question.question)
