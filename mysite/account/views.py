from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from django.conf import settings

def registration_view(request):
	template = loader.get_template('register.html')
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			return redirect('login')
		else:
			context['registration_form'] = form
	else: #GET request
		form = RegistrationForm()
		context['registration_form'] = form
		
	return HttpResponse(template.render(context, request))

def logout_view(request):
	logout(request)
	return redirect('index') 

def login_view(request):
    template = loader.get_template('login.html')

    context = {}

    user = request.user

    if user.is_authenticated:
        return redirect('index')
    
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            
            if user:
                login(request, user)
                return redirect('index')
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return HttpResponse(template.render(context, request))

def account_view(request):
	template = loader.get_template('account.html')

	if not request.user.is_authenticated:
		return redirect("login")

	context = {}

	if request.POST:
		form = AccountUpdateForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
	else:
		form = AccountUpdateForm(
				initial= {
					"email": request.user.email,
					"username": request.user.username,
				}
			)
	context['account_form'] = form
	return HttpResponse(template.render(context, request))

def password_reset_view(request):
    template = loader.get_template('password_reset(sample).html')

    context = {}

    if request.method=="post":
        email = request.post('email')
        send_mail(
        'Reset Password',
        'settings.EMAIL_HOST_USER',
        [email],
        fail_silently = False
		)
    return HttpResponse(template.render(context, request))