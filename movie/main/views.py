from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView

from .models import *
# Create your views here.
class HomeView(ListView):
    """Home Page View for movies"""
    model = Movie
    paginate_by = 6
    # template_name = "main/movie_list.html"
    # context_object_name = "paypoq" #or object_list 
    

class MovieDetailView(DetailView):
    model = Movie
    # template_name = ''
    # context_object_name = "paypoq" #or object or movie
    
class CategoryListView(ListView):
    model = Category     
    
    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Movie.objects.filter(category=self.category)
    
class GenreListView(ListView):
    model = Genre     
    
    def get_queryset(self):
        self.genre = get_object_or_404(Genre, slug=self.kwargs['slug'])
        return Movie.objects.filter(genre=self.genre)
    
class ActorDetailView(DetailView):
    model = Actors
    template_name = 'main/actor_detail.html'
    
    
