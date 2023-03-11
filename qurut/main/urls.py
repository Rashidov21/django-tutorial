from django.urls import path 
from .import views 

app_name = 'main'

urlpatterns = [
    path("", views.homePageView, name='home'),
    path("quruts/", views.qurutsPageView, name='quruts'),
]
