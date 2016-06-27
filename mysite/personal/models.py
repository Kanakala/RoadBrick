from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
	
	from1 = models.CharField(max_length=20)
	type_of_truck = models.CharField(max_length=20)
	date = models.CharField(max_length=20)
	weight = models.DecimalField( max_digits=5, decimal_places=2)
	Material_Name = models.CharField(max_length=20)
	To = models.CharField(max_length=20)
	Number_Of_Truck = models.CharField(max_length=20)
	Time = models.CharField(max_length=20)
	Volume = models.CharField(max_length=20)
	Material_Type = models.CharField(max_length=20)
	#updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    

	
	def __unicode__(self):
		return self.from1

	def __str__(self):
		return self.from1

	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"id": self.id})
		

	# def __unicode__(self):
		# return self.user.username