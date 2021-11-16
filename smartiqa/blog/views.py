from django.shortcuts import render
from .models import *
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
    context = {"object":post}
    return render(request, "detail.html",context)

def categoryDetail(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    post = Post.objects.filter(category=category)
    print(post)
    context = {"objects": post}
    return render(request, "categories.html", context)

