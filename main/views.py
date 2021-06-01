from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.


def homePage(request):
	posts = Post.objects.all() # Post models dan hamma obyektlarni oladi
	# get , filter , create, order_by, delete, save
	# for post in posts:
	# 	print(post.title)
	context = {
		'posts':posts
	}
	return render(request, 'index.html',context)



def aboutPage(request):
	return render(request, 'about.html')

def postPage(request):
	return render(request, 'post-details.html')

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

def postDetailPage(request, post_slug):
	post = Post.objects.get(slug=post_slug)
	return render(request, 'post-details.html', {'post':post})