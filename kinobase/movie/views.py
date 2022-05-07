from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.
from .models import Movie



class HomeView(ListView):
    model = Movie
    template_name = 'index.html'

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie-detail.html'
