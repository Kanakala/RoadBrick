from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
# from personal.forms import MyRegistrationForm
from personal.forms import *
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect


from .forms import PostForm
from .models import Post





def index(request):
    return render(request, 'before_login/index.html')

def deal(request):
	queryset = Post.objects.all()
	context = {
		"object_list": queryset, 
		"title": "List"
	}
	return render(request, 'before_login/deal.html', context)
	
def post_detail(request, id=None): #retrieve
	#instance = Post.objects.get(id=1)
	instance = get_object_or_404(Post, id=id)
	context = {
		"title": instance.from1,
		"instance": instance,
	}
	return render(request, "loggedin_load/post_detail.html", context)

def registration(request):
    return render(request, 'before_login/registration.html')

def truckprovider(request):
    return render(request, 'before_login/truckprovider.html')

def loadprovider(request):
    return render(request, 'before_login/loadprovider.html')

@csrf_protect
def register_view(request):
	title = "Register"
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(
			username=form.cleaned_data['username'],
			password=form.cleaned_data['password1'],
			email=form.cleaned_data['email']
			)
			return HttpResponseRedirect('/register/success/')
	else:
		form = RegistrationForm()
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
def home(request):
    return render_to_response(
    'home.html',
    { 'user': request.user }
    )


# def post_load(request):
	# return render(request, 'loggedin_load/post_load.html')

def post_load(request):
	return render(request, 'loggedin_load/post_load.html')

	
def profile_view(request):
	return render(request, 'loggedin_load/profile.html')
	
def profile_settings(request):
	return render(request, 'loggedin_load/profile_settings.html')
	
def live_bids(request):
	return render(request, 'loggedin_load/live_bids.html')
	
def active_deals(request):
	return render(request, 'loggedin_load/active_deals.html')
	
def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		print(form.cleaned_data.get("from1"))
		instance.save()

	# if request.method == "POST":
	# 	print "title" + request.POST.get("content")
	# 	print request.POST.get("title")
	# 	#Post.objects.create(title=title)
	context = {
		"form": form,
	}
	return render(request, "loggedin_load/post_load.html", context)

	return render(request, 'loggedin_load/live_bids.html')

