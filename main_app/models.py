from django.db import models

# Create your models here.
class Data(models.Model):
	title = models.CharField(max_length=500)
	pref = models.CharField(max_length=500)
