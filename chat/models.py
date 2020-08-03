from django.db import models


class Room(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(default='chat_default.png',
                              upload_to='chat_images')

    def __str__(self):
        return self.title
