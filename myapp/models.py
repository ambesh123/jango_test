from django.db import models
from django.utils import timezone

# Create your models here.

class Person(models.Model):
	name = models.CharField(max_length=20)
	mobile = models.CharField(max_length=10,primary_key=True)
	SEX = (
			('M','MALE'),
			('F','FEMALE')
		)
	gender = models.CharField(max_length=1,choices = SEX)

	dob = models.DateField(default = timezone.now)

	def done(self):
		self.save()

	def __str__(self):
		return self.mobile

class Photo(models.Model):
	desc = models.CharField(max_length=30 , blank = True , null = True)
	doc = models.ImageField(upload_to = 'documents/')
