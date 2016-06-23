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
	url(r'^accounts/profile/$', views.profile_view, name='profile_view'),

    url(r'^deal/$', views.deal, name='deal'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^truckprovider/$', views.truckprovider, name='truckprovider'),
    url(r'^loadprovider/$', views.loadprovider, name='loadprovider'),
    
]
