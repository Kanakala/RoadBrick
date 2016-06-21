from django.conf.urls import patterns, url, include
from django.contrib import admin
admin.autodiscover()
#from django.contrib.auth.views import login, logout #views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls'))
    url(r'^admin/', admin.site.urls),
    # url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    # url(r'^accounts/auth/$', 'personal.views.auth_view'),
    # #url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    # url(r'^accounts/loggedin/$', 'personal.views.loggedin'),
    # url(r'^accounts/invalid/$', 'personal.views.invalid'),
	url(r'^login/', views.login_view, name='login'),
	url(r'^logout/', views.logout_view, name='logout'),
	url(r'^register/', views.register_view, name='register'),
    url(r'^accounts/register/$', 'personal.views.register'),
    url(r'^accounts/register_success/$', 'personal.views.register_success'),

    url(r'^deal/$', views.deal, name='deal'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^truckprovider/$', views.truckprovider, name='truckprovider'),
    url(r'^loadprovider/$', views.loadprovider, name='loadprovider'),
    
]
