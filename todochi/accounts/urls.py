from django.urls import path
from .import views

app_name = 'accounts'

urlpatterns = [
    path("login/", views.my_login, name='login'),
    path("logout/", views.logged_out, name='logout'),
    path("register/", views.my_register_view, name='register'),
]

