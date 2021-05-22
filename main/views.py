from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.


def homePage(request):
	return render(request, 'index.html')

def aboutPage(request):
	return render(request, 'about.html')

def contactPage(request):	
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']
		Contact.objects.create(
			name=name,email=email,
			subject=subject,message=message
			)
		messages.add_message(request,messages.SUCCESS ,'Contact saved !')
		return render(request, 'contact.html')
	else:
		messages.add_message(request,messages.WARNING ,'Contact not saved !')

		
	return render(request, 'contact.html')