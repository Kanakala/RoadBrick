from django.db import models
from django.contrib.auth.models import User

class register(models.Model):
	username = models.CharField(max_length=100)
	email = models.EmailField(max_length=70,blank=True)
	password = models.CharField(max_length=30)
	password_confirmation = models.CharField(max_length=30)
    

	def __str__(self):
		return self.title

		

	# def __unicode__(self):
		# return self.user.username