from django.db import models

# Create your models here.
class Users(models.Model):
	uname = models.CharField(max_length = 20 , primary_key = True)
	pwd = models.CharField(max_length = 20)
