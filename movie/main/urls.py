from  django.urls import path 
from django.views.generic import TemplateView
from . import views
app_name = 'main'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('test/', TemplateView.as_view(
        template_name="test.html"), name='test'),
    path('detail/<slug:slug>/', views.MovieDetailView.as_view(), name='detail'),
    path('category/<slug:slug>/', views.CategoryListView.as_view(), name='category_list'),
    path('genre/<slug:slug>/', views.GenreListView.as_view(), name='genre_list'),
    path('actor/<pk>/', views.ActorDetailView.as_view(), name='actor_detail'),
]