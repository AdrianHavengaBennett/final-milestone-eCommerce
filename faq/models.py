from django.db import models


class FAQ(models.Model):
	question = models.CharField(max_length=250, blank=False)
	answer = models.TextField()

	def __str__(self):
		return self.question
