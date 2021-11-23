from django.shortcuts import render
from .models import *
from .forms import CommentForm
# from django.views.generic.base import (
# TemplateView, View
# )
# Create your views here.

# class HomeView(TemplateView):
#     template_name = "index.html"
def homeView(request):
    tags = Tag.objects.all()
    posts = Post.objects.all()
    context = {"tags":tags, "posts":posts}
    return render(request, "index.html", context)

def postDetail(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.post = post
            f.save()
    else:
        form = CommentForm()
        print("NOT " * 5)

    context = {"object":post, "form":form}
    return render(request, "detail.html",context)

def categoryDetail(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    post = Post.objects.filter(category=category)
    print(post)
    context = {"objects": post}
    return render(request, "categories.html", context)

def tagDetail(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    posts = Post.objects.filter(tag=tag)
    context = {"objects": posts}
    return render(request, "categories.html",context)

def contactView(request):
    return render(request, "contact.html")
