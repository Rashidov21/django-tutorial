from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView 



# Create your views here.
from .forms import AddNewTodoForm
from .models import Todo


class TodoView(TemplateView):
    template_name = 'index.html'
    extra_context = {"form":AddNewTodoForm()}



class AddNewTodo(CreateView):
    model = Todo
    form_class = AddNewTodoForm
    success_url = '/'