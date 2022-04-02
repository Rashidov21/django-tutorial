from django.urls import path 
from . import views


app_name = "main"

urlpatterns = [
    path("", views.index, name="homePage"),
    path("/contact/", views.contact, name="contactPage"),
]
