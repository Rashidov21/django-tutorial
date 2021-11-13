from django.shortcuts import render
from .models import  Tag, Post
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


