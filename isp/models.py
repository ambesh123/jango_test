from django.db import models

class Isp(models.Model):
	name = models.CharField(max_length = 20 , primary_key = True)
	price = models.CharField(max_length=10)
	rating = models.IntegerField(null = True)
	maxSpeed = models.CharField(max_length=10 , null = True)
	desc = models.TextField(null = True)

	def __str__(self):
		return self.name
