from django.contrib import admin

from django.db import models
from . models import Bid, Auction

class BidModelAdmin(admin.ModelAdmin):
	
	list_filter = ( 'amount',)
	class Meta:
		model = Bid

admin.site.register( Bid, BidModelAdmin)
admin.site.register(Auction)
