from django.conf.urls import patterns, url, include
from django.contrib import admin
admin.autodiscover()
#from django.contrib.auth.views import login, logout #views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls'))
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', views.register_view, name='register'),
    url(r'^register/success/$', views.register_success, name='register_success'),
    url(r'^home/$', views.home, name='home'),
	url(r'^post_load/$', views.post_create, name='post_create'),
	url(r'^profile/$', views.profile_view, name='profile_view'),
	url(r'^profile_settings/$', views.profile_settings, name='profile_settings'),
	url(r'^live_bids/$', views.live_bids, name='live_bids'),
	url(r'^active_deals', views.active_deals, name='active_deals'),

    url(r'^deal/$', views.deal, name='deal'),
	url(r'^deal/(?P<id>\d+)/$', views.post_detail, name='detail'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^truckprovider/$', views.truckprovider, name='truckprovider'),
    url(r'^loadprovider/$', views.loadprovider, name='loadprovider'),
    
]
