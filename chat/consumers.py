import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
# from .models import Thread, ChatMessage


class ChatConsumer(AsyncConsumer):
	async def websocket_connect(self, event):
		"""When the socket connects"""
		print('connected', event)

	async def websocket_connect(self, event):
		"""When a message is received from a websocket"""
		print('received', event)

	async def websocket_connect(self, event):
		"""When the socket disconnects"""
		print('disconnected', event)
