from django.conf.urls import patterns, url, include
from django.contrib import admin
admin.autodiscover()
#from django.contrib.auth.views import login, logout #views as auth_views
from . import views
from custom_user.forms import LoginForm

urlpatterns = [
	url(r'^', include('django.contrib.auth.urls')),
	url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register_view, name='register'),
    url(r'^register/success/$', views.register_success, name='register_success'),
	url(r'^truckprovider/$', views.truckprovider, name='truckprovider'),
	url(r'^truck_profile', views.truck_profile_view, name='truck_profile_view'),
	url(r'^live_bid_truck', views.live_bid_truck, name='live_bid_truck'),
	url(r'^truck_profile_settings', views.truck_profile_settings, name='truck_profile_settings'),
	url(r'^live_deal', views.live_deal, name='live_deal'),
	
	]
	