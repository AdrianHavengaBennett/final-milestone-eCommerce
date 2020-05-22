from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class BlogPost(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	content = models.TextField()
	date_created = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title
