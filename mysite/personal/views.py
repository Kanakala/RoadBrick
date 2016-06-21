from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
# from personal.forms import MyRegistrationForm
from personal.forms import UserForm, UserLoginForm, UserRegisterForm
from django.template import RequestContext

def index(request):
    return render(request, 'personal/index.html')

def deal(request):
    return render(request, 'personal/deal.html')

def registration(request):
    return render(request, 'personal/registration.html')

def truckprovider(request):
    return render(request, 'personal/truckprovider.html')

def loadprovider(request):
    return render(request, 'personal/loadprovider.html')

def login_view(request):
	print(request.user.is_authenticated())
	title = "Login"
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		login(request, user)
		print(request.user.is_authenticated())
		return redirect("/")
	return render(request, "registration/form.html", {"form":form, "title":title})
	
def logout_view(request):
	logout(request)
	return redirect("/")
	
@csrf_protect
def register_view(request):
	title = "Register"
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		user = User.objects.create_user(
		new_user = authenticate(username=user.username, password=password))
		login(request, new_user)
		return redirect("/")
	
	context = {
		"form": form,
		"title": title
	}
	return render(request, "registration/form.html", context)
	
# def login(request):
    # c = {}
    # c.update(csrf(request))
    # return render_to_response('registration/login.html', c)

# def auth_view(request):
   # username = request.POST.get('username', '')
   # password = request.POST.get('password', '')
   # user = auth.authenticate(username=username, password=password)
   
   # if user is not None and user.is_active:
        # auth.login(request, user)
        # return HttpResponseRedirect('/accounts/loggedin/')
   # else:
	    # return HttpResponseRedirect('/accounts/invalid')

# def loggedin(request):
    # return render_to_response('registration/loggedin.html',
                              # {'full_name': request.user.username})

# def invalid(request):
    # return render_to_response('registration/invalid.html')

#def logout(request):
#    auth.logout(request)
#    return render_to_response('registration/logout.html')

# def register_user(request):
   # if request.method == 'POST':
        # form = MyRegistrationForm(request.POST)
        # if form.is_valid():
            # form.save()
            # return HttpResponseRedirect('/accounts/register_success')

        # args = {}
        # args.update(csrf(request))

        # args['form'] = MyRegistrationForm()

        # return render_to_response('registration/register.html', args)

# def register_success(request):
    # return render_to_response('registration/register_success.html')

def register(request):
	registered = False

    # If it's a HTTP POST, we're interested in processing form data.
	if request.method == 'POST':
        
		user_form = UserForm(data=request.POST)
        

        
		if user_form.is_valid():
           
			user = user_form.save()

            
			user.set_password(user.password)
			user.save()
                     
			registered = True

        
		else:
			print (user_form.errors)

    
	else:
		user_form = UserForm()
        

    
	return render_to_response(
            'registration/register.html',
            {'user_form': user_form, 'registered': registered}, 
			context_instance=RequestContext(request))
		
def register_success(request):
    return render_to_response('registration/register_success.html')
