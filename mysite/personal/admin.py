from django.contrib import admin
from django.db import models
from .models import Post

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class PostModelAdmin(admin.ModelAdmin):
	list_display = [ "type_of_truck", "date", "weight", "Material_Name", "To", "Number_Of_Truck", "Time", "Volume", "Material_Type", "timestamp"]
	#list_display_links = ["from1"]
	list_editable = ["weight"]
	list_filter = [ "from1", "timestamp"]

	search_fields = ["from1", "type_of_truck", "date", "weight", "Material_Name", "To", "Number_Of_Truck", "Time", "Volume", "Material_Type", "timestamp"]
	class Meta:
		model = Post

admin.site.register( Post, PostModelAdmin)
