from  django.urls import path 
from django.views.generic import TemplateView
from . import views
app_name = 'main'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('test/', TemplateView.as_view(
        template_name="test.html"), name='test'),
]