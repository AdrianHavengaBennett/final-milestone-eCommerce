from django.db import models


class ClickCollectLocations(models.Model):
	location_name = models.CharField(max_length=40)
	street_address1 = models.CharField(max_length=40)
	street_address2 = models.CharField(max_length=40, blank=True)
	town_or_city = models.CharField(max_length=40)
	postcode = models.CharField(max_length=40)
	location_email = models.EmailField()
	location_phone = models.CharField(max_length=40)

	def __str__(self):
		return self.location_name
