from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from personal.models import Contact

def index_view(request):
    template = loader.get_template('index.html')

    context = {}

    if request.method=="POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        return render(request, "contact_done.html")

    return HttpResponse(template.render(context, request))
