import datetime
from haystack import indexes
from .models import Post
from django.contrib.auth import authenticate, get_user_model

class PostIndex(indexes.SearchIndex,indexes.Indexable):
	text = indexes.CharField(document=True,use_template=True)
	type_of_truck = indexes.CharField(model_attr='type_of_truck')
	date = indexes.DateField(model_attr='date')
	#slug = indexes.SlugField(unique=True)
	weight = indexes.DecimalField(model_attr='weight')
	Material_Name = indexes.CharField(model_attr='Material_Name')
	To = indexes.CharField(model_attr='To')
	Number_Of_Truck = indexes.CharField(model_attr='Number_Of_Truck')
	#Time = indexes.TimeField()
	Volume = indexes.CharField(model_attr='Volume')
	Material_Type = indexes.CharField(model_attr='Material_Type')
	
	content_auto = indexes.EdgeNgramField(model_attr='from1')
	
	def get_model(self):
		return Post
	def index_queryset(self,using=None):
			"""used when entire index for model is updated."""
			return self.get_model().objects.all()	