from django.db import models

# Create your models here.

class Sweet(models.Model):
	name = models.CharField(max_length=200)
	price = models.PositiveIntegerField()
	image = models.ImageField()
	description = models.CharField(max_length=500, blank=True, null=True)


	def __str__(self):
		return self.name