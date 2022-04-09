from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('search/', views.inlineSearch, name='search'),
    path('detail/<slug:slug>', views.PostDetailView.as_view(), name='detail'),
    path("category/<slug:category_slug>/", views.category_list, name='category_list')
]
# paths    