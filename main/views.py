from django.shortcuts import render
from .models import Contact
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
		print(name,email,subject,message)
		Contact.objects.
	return render(request, 'contact.html')