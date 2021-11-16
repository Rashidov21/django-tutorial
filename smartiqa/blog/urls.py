from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.homeView, name='home'),
    path("detail/<slug:post_slug>", views.postDetail, name='post_detail'),
    path("<slug:category_slug>", views.categoryDetail, name='category_detail'),
]