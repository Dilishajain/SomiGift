from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Images(models.Model) :
	title = models.CharField(max_length=100)
	photo = models.ImageField(upload_to = 'static/somi/',null = True)

	def __str__(self):
		return self.title