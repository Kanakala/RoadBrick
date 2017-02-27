from django.shortcuts import render, render_to_response, redirect, get_object_or_404, RequestContext
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib import auth
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
#from personal.forms import MyRegistrationForm
from custom_user.forms import EmailUserChangeForm, EmailUserCreationForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm
# from . forms import CustomUserForm
from personal.forms import *
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from custom_user.models import User
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User, Group
from urllib.parse import quote_plus
from haystack.query import SearchQuerySet
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.utils import timezone

from .forms import PostForm
from .models import Post





def index(request):
    return render(request, 'before_login/index.html')
	
def not_in_company_group(user):
    if user:
        return user.groups.filter(name='Company').count() == 0
    return False
	
def not_in_truck_group(user):
    if user:
        return user.groups.filter(name='Truck').count() == 0
    return False	


@login_required	
@user_passes_test(not_in_company_group, login_url='/login/')
def post_create(request):
	# if not request.user.is_staff or not request.user.is_superuser:
		# raise Http404
		
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		print(form.cleaned_data.get("from1"))
		instance.user = request.user
		instance.save()
		# message success
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, "loggedin_load/post_load.html", context)

def deal(request):
	today = timezone.now().date()
	queryset_list = Post.objects.active() #.order_by("-timestamp")
	if request.user.is_staff or request.user.is_superuser:
		queryset_list = Post.objects.all()
	
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
				Q(from1__icontains=query)|
				Q(type_of_truck__icontains=query)|
				Q(Material_Name__icontains=query) |
				Q(To__icontains=query)|
				Q(Material_Type__icontains=query)
				).distinct()
	paginator = Paginator(queryset_list, 2) # Show 25 contacts per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)


	context = {
		"object_list": queryset_list, 
		"from1": "List",
		"page_request_var": page_request_var,
		"today": today,
	}
	return render(request, 'before_login/deal.html', context)



	
@login_required	
@user_passes_test(not_in_company_group, login_url='/login/')	
def post_detail(request, slug=None): #retrieve
	#instance = Post.objects.get(id=1)
	instance = get_object_or_404(Post, slug=slug)
	if instance.date > timezone.now().date():
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	share_string = quote_plus(instance.Material_Type)
	context = {
		"from1": instance.from1,
		"instance": instance,
		"share_string": share_string
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
 
def login(request):
    c = {}
    c.update(csrf(request))    
    return render(request, 'login.html', c)

	
def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    form = LoginForm(data=request.POST)
    if user is not None:
        if user.is_active:
            login(request, user)
            if form.is_valid():
                user_type = form.cleaned_data['Label']
                if user_type == 'Truck':
                    return HttpResponseRedirect('/post_load/')
                elif user_type == 'Company':
                    return HttpResponseRedirect('/live_deal/')
				
            # Redirect to a success page.
        # else:
            # Return a 'disabled account' error message
            ...
    else:
        form = LoginForm()
		# Return an 'invalid login' error message.
        ...
@csrf_protect
# def login_view(request):
	# title = "Login"
	
	# if request.method == 'POST':
		
		# form = LoginForm(data=request.POST)
		# if form.is_valid():
			# user_type = form.cleaned_data['Label']
			# if user_type == 'Truck':
				# return HttpResponseRedirect('/post_load/')
			# elif user_type == 'Company':
				# return HttpResponseRedirect('/live_deal/')
	# else:
		# form = LoginForm()

	# return render(request, 'registration/login.html', {'form' : form, 'title': title})


	
@login_required
def home(request):
	if User.groups.filter(name='Truck') == True:
		return render_to_response("loggedin_truck/live_deal.html", locals(),
                      context_instance=RequestContext(request))
	else:
		return render_to_response("loggedin_load/post_load.html", locals(),
              context_instance=RequestContext(request))
    
# def auth_view(request):
    # username = request.POST.get('username', '')
    # password = request.POST.get('password', '')
    # user = auth.authenticate(username=username, password=password)
    
    # if user is not None:
        # auth.login(request, user)
        # return HttpResponseRedirect('/accounts/loggedin')
    # else:
        # return HttpResponseRedirect('/accounts/invalid')
 
 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
 
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
 
# @login_required
# def home(request):
    # return render_to_response(
    # 'home.html',
    # { 'user': request.user }
    # )


# def post_load(request):
	# return render(request, 'loggedin_load/post_load.html')

@login_required	
@user_passes_test(not_in_company_group, login_url='/login/')
def post_load(request):
	return render(request, 'loggedin_load/post_load.html')

@login_required	
@user_passes_test(not_in_company_group, login_url='/login/')	
def profile_view(request):
	return render(request, 'loggedin_load/profile.html')

@login_required	
@user_passes_test(not_in_company_group, login_url='/login/')	
def profile_settings(request):
	return render(request, 'loggedin_load/profile_settings.html')

@login_required	
@user_passes_test(not_in_company_group, login_url='/login/')	
def live_bids(request):
	return render(request, 'loggedin_load/live_bids.html')

@login_required	
@user_passes_test(not_in_company_group, login_url='/login/')	
def active_deals(request):
	return render(request, 'loggedin_load/active_deals.html')



@login_required
@user_passes_test(not_in_truck_group, login_url='/login/')
def live_bid_truck(request):
	queryset = Post.objects.all()
	context = {
		"object_list": queryset, 
		"title": "List"
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
	



# def post_create(request):
	# form = PostForm(request.POST or None)
	# if form.is_valid():
		# instance = form.save(commit=False)
		# print(form.cleaned_data.get("from1"))
		# instance.save()

	# if request.method == "POST":
		# print "title" + request.POST.get("content")
		# print request.POST.get("title")
		#Post.objects.create(title=title)
	# form.fields['from1'].widget.attrs['class'] = "form-control" 
	# context = {
		# "form": form,
	# }


	

