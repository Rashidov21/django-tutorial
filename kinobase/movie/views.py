from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect ,HttpResponse
from django.views.generic import ListView, DetailView
from django.contrib.auth import authenticate, login
# Create your views here.
from .models import *

def category_list(request,slug):
    category = Category.objects.get(slug=slug) #Фильмы
    movies = Movie.objects.filter(category=category)
   
    paginator = Paginator(movies, 2) # Show 2 movies per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'list.html', {'page_obj': page_obj})

def my_login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return HttpResponse("Success !")
    
    else:
        # Return an 'invalid login' error message.
        return render(request, "login.html")
    
    return render(request, "login.html")

class HomeView(ListView):
    model = Movie
    template_name = 'index.html'

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie-detail.html'

