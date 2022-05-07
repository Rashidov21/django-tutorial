from django.urls import path
from .import views

app_name= 'movie'

urlpatterns = [
    path("", views.HomeView.as_view(), name='home'),
    path("movie/<slug:slug>/", views.MovieDetailView.as_view(), name='detail')
]