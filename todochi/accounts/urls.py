from django.urls import path
from .import views

from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    # path("login/", views.my_login, name='login'),
    # path("logout/", views.logged_out, name='logout'),
    path("register/", views.my_register_view, name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/update/<int:pk>', views.ProfileUpdateView.as_view(), name='profile_update'),
    # Standart Auth views from Django 
    path("login/", auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path("logout/", auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
    
    
    
]

