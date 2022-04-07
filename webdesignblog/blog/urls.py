from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('detail/<slug:slug>', views.PostDetailView.as_view(), name='detail'),
]
