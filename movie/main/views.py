from django.shortcuts import render
from django.views.generic import ListView

from .models import Movie
# Create your views here.
class HomeView(ListView):
    """Home Page View for movies"""
    model = Movie
    paginate_by = 5
    template_name = "index.html"
    
