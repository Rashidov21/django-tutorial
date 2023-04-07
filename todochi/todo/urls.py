from django.urls import path 
from . import views 

app_name = 'todo'

urlpatterns = [
    path('', views.TodoView.as_view(), name='home'),
    path("add/", views.AddNewTodo.as_view(), name='add'),
]
