from django.db import models
from django.contrib.auth.models import User

from PIL import Image


# Override User model email, first_name, and last_name fields
User._meta.get_field('email')._unique = True
User._meta.get_field('email').blank = False
User._meta.get_field('email').null = False

User._meta.get_field('first_name').blank = False
User._meta.get_field('first_name').null = False

User._meta.get_field('last_name').blank = False
User._meta.get_field('last_name').null = False


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(
        default='default.jpg', upload_to='profile_images')

    DEFAULT = 'default-scheme'
    RED = 'red-scheme'
    BLUE = 'blue-scheme'
    GREEN = 'green-scheme'
    PINK = 'pink-scheme'
    PURPLE = 'purple-scheme'
    YELLOW = 'yellow-scheme'
    COLOR_SCHEME_CHOICES = [
        (DEFAULT, 'Default'),
        (RED, 'Red'),
        (BLUE, 'Blue'),
        (GREEN, 'Green'),
        (PINK, 'Pink'),
        (PURPLE, 'Purple'),
        (YELLOW, 'Yellow'),
    ]
    color_scheme = models.CharField(
        max_length=14,
        choices=COLOR_SCHEME_CHOICES,
        default=DEFAULT,
    )

    def __str__(self):
        return self.user.username
