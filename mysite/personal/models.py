from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import pre_save
from django.utils import timezone
from datetime import datetime
from django.utils.text import slugify

class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        # Post.objects.all() = super(PostManager, self).all()
        return super(PostManager, self).filter(Time__lte=timezone.now())



class Post(models.Model):
	
	id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	from1 = models.CharField(max_length=20)
	type_of_truck = models.CharField(max_length=20)
	date = models.DateField()
	slug = models.SlugField(unique=True)
	weight = models.DecimalField( max_digits=5, decimal_places=2)
	Material_Name = models.CharField(max_length=20)
	To = models.CharField(max_length=20)
	Number_Of_Truck = models.CharField(max_length=20)
	Time = models.TimeField()
	Volume = models.CharField(max_length=20)
	Material_Type = models.CharField(max_length=20)
	#updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    
	objects = PostManager()
	
	def __unicode__(self):
		return self.from1

	def __str__(self):
		return self.from1

	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"slug": self.slug})

	class Meta:
		ordering = ["-timestamp", "-Time"]
		



def create_slug(instance, new_slug=None):
    slug = slugify(instance.id)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)



pre_save.connect(pre_save_post_receiver, sender=Post)
