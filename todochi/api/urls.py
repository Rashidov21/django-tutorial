from django.urls import path 
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.HomeApiView.as_view(), name='home_api')
]
