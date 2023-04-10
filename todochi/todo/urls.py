from django.urls import path 
from . import views 

app_name = 'todo'

urlpatterns = [
    path('', views.TodoView.as_view(), name='home'),
    path("add/", views.AddNewTodo.as_view(), name='add'),
    path("detail/<pk>", views.TodoDetailView.as_view(), name='detail'),
    
    path("delete/<int:todo_id>", views.TodoDeleteView.as_view(), name='delete'),
    path("update/<pk>", views.TodoUpdateView.as_view(), name='update'),
    path("done/<int:todo_id>", views.TodoDoneView.as_view(), name='done')
]
