from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
# Create your views here.
from .models import *

def category_list(request,slug):
    category = Category.objects.get(slug=slug) #Фильмы
    movies = Movie.objects.filter(category=category)
   
    paginator = Paginator(movies, 2) # Show 2 movies per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'list.html', {'page_obj': page_obj})



class HomeView(ListView):
    model = Movie
    template_name = 'index.html'

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie-detail.html'

