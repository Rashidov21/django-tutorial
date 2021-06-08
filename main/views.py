from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponse
from django.contrib import messages
from .forms import AddCommentForm

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
	if request.method == 'POST':
		form = AddCommentForm(request.POST)
		if form.is_valid():
			f = form.save(commit=False)
			f.post = post
			f.save()
	else:
		form = AddCommentForm()
	post.views += 1
	context = {
		'post':post,
		'form':form
	}
	return render(request, 'post-details.html', context)

def categoryDetailPage(request, category_slug):
	category = get_object_or_404(Category, slug=category_slug)
	print(category)
	post = Post.objects.filter(category=category)
	return  render(request, 'post_list.html',{'post':post})

def tagDetailPage(request, tag_slug):
	tag = get_object_or_404(Tags, slug=tag_slug)
	print(tag)
	post = Post.objects.filter(tag=tag)
	return  render(request, 'post_list.html', {'post':post})