from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from personal.models import Post

class Bid(models.Model):
	
	post_id = models.ForeignKey(Post)
	user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True, unique = False)
	amount = models.IntegerField()
	
	def get_absolute_url(self):
		return reverse("accept_bid", kwargs={"id": self.id})
	
	def __unicode__(self):
		return self.amount

	def __str__(self):
		return self.amount

class Auction(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    accepted_bid = models.ForeignKey(Bid)

