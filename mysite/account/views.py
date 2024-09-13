from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
from django.http import HttpResponse
from django.template import loader

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

def terms_and_conditions_view(request):
    template = loader.get_template('terms_and_conditions.html')
    return HttpResponse(template.render({}, request))

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
				# Prevent superusers from logging in through user login
                if user.is_superuser:
                    context['login_form'] = form
                    context['error_message'] = "Admin account cannot log in here."
                    return HttpResponse(template.render(context, request))
				
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