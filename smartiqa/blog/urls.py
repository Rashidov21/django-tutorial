from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.homeView, name='home'),
    path("contact/", views.contactView, name="contact"),
    path("detail/<slug:post_slug>", views.postDetail, name='post_detail'),
    path("category/<slug:category_slug>/", views.categoryDetail, name='category_detail'),
]