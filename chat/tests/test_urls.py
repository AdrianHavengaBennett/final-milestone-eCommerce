from django.test import SimpleTestCase
from django.urls import reverse, resolve

from chat.views import chat, room


class TestUrls(SimpleTestCase):
    """The following tests the urls"""

    def test_chat_url_resolves(self):
        url = reverse('chat')
        self.assertEquals(resolve(url).func, chat)

    def test_room_url_resolves(self):
        url = reverse('room', args=[1])
        self.assertEquals(resolve(url).func, room)
