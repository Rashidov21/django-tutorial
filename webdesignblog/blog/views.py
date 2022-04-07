from django.shortcuts import render
from .models import Post
# from django.views.generic.base import TemplateView
from django.views.generic import ListView
# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = "index.html"
    