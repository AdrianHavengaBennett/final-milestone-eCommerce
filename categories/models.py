from django.db import models


class Category(models.Model):
	category_name = models.CharField(max_length=40)
	image = models.ImageField(default='product_default.png', upload_to='category_images')

	def __str__(self):
		return self.category_name
