from django.db import models

from categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    category_name = models.ForeignKey(
        Category, on_delete=models.CASCADE, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(
        default='product_default.png', upload_to='product_images')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('image', )
