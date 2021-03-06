from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from products.models import Product
from shows.models import UpcomingShows


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    product = models.ForeignKey(Product, on_delete=models.PROTECT,
                                default='', null=True)
    show = models.ForeignKey(UpcomingShows, on_delete=models.PROTECT,
                             default='', null=True)

    class Meta:
        ordering = [
            '-date_created'
        ]

    def __str__(self):
        return self.title
