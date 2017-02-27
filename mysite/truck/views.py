from django.shortcuts import render, render_to_response, redirect, get_object_or_404, RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
#from personal.forms import MyRegistrationForm
from custom_user.forms import EmailUserChangeForm, EmailUserCreationForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm
# from . forms import CustomUserForm

from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from custom_user.models import User
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User, Group
from . models import Bid
from personal.models import Post
from . forms import BidForm


def not_in_truck_group(user):
    if user:
        return user.groups.filter(name='Truck').count() == 0
    return False


def registration(request):
    return render(request, 'before_login/registration.html')

def truckprovider(request):
    return render(request, 'before_login/truckprovider.html')

@csrf_protect
def register_view(request):
	title = "Register"
	global user
	if request.method == 'POST':
		form = EmailUserCreationForm(request.POST)
		if form.is_valid():
			# user = User.objects.create_user(
			# username=form.cleaned_data['username'],
			# password=form.cleaned_data['password1'],
			# email=form.cleaned_data['email'],
			# form = RadioSelection()
			
			# )
			form.save()
			return HttpResponseRedirect('/register/success/')
	else:
		form = EmailUserCreationForm()
	variables = RequestContext(request, {
	'form': form,
	'title': title
	})
 
	return render_to_response(
	'registration/form.html',
	variables,
	)

def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
 
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
@user_passes_test(not_in_truck_group, login_url='/login/')
def live_bid_truck(request):
	form = BidForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		print(form.cleaned_data.get("amount"))
		instance.user = request.user
		instance.save()
		
	
	
	queryset = Post.objects.all()
	context = {
		"form": form,
		"object_list": queryset, 
		"title": "List",
		
	}
	return render(request, 'loggedin_truck/live_bid_truck.html', context)

def rank(request):
	
	bid_queryset = Bid.objects.all().order_by('amount')
	

	current_rank = 1
	counter = 0

	for bid in bid_queryset:
		if counter < 1: # for first bid
			bid.rank = current_rank
		else: # for other bids
			if bid.amount == bid_queryset[counter - 1].amount:
            # if bid and previous bid have same score,
            # give them the same rank
				bid.rank = current_rank
			else:
            # first update the rank
				current_rank += 1
            # then assign new rank to bid
				bid.rank = current_rank
		counter += 1
		
	
	context = {
		"bid_queryset": bid_queryset,
		"title": "List",
	}
	return render(request, 'loggedin_truck/live_bid_truck.html', context)
	
@login_required
@user_passes_test(not_in_truck_group, login_url='/login/')
def live_deal(request):
	return render(request, 'loggedin_truck/live_deal.html')

@login_required
@user_passes_test(not_in_truck_group, login_url='/login/')	
def truck_profile_view(request):
	return render(request, 'loggedin_truck/truck_profile.html')

@login_required
@user_passes_test(not_in_truck_group, login_url='/login/')	
def truck_profile_settings(request):
	return render(request, 'loggedin_truck/truck_settings.html')
	
