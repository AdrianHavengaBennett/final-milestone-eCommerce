from django.test import TestCase
from chat.models import Room


class TestRoomModel(TestCase):
	"""The following tests the Room model"""

	def test_chat_string_method_returns_title(self):
		room = Room.objects.create(title='Test Room')
		
		self.assertEqual(room.__str__(), room.title)
