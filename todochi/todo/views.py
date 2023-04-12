import datetime
from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.views.generic.edit import CreateView , DeleteView, UpdateView



# Create your views here.
from .forms import AddNewTodoForm
from .models import Todo


class TodoView(ListView):
    model = Todo
    template_name = 'index.html'
    # object_list or ;
    context_object_name = 'todos'
    
    # def get_queryset(self):
    #     queryset = Todo.objects.filter(done=False)
    #     return queryset
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context["doned_false"] = Todo.objects.filter(done=False) 
        context["doned_true"] = Todo.objects.filter(done=True) 
        return context
    
    # extra_context = {"form":AddNewTodoForm()}

class TodoDetailView(DetailView):
    model = Todo

# class TodoDeleteView(DeleteView):
#     model = Todo
#     success_url = '/'
class TodoDeleteView(View):
    
    def get(self, request,todo_id, *args, **kwargs):
        todo = Todo.objects.get(pk=todo_id)
        todo.delete()
        return redirect("/")
    
class TodoDoneView(View):
    
    def get(self, request, todo_id,*args, **kwargs):
        print(self.request.path)
        todo = Todo.objects.get(pk=todo_id)
        todo.done = True
        todo.doned_at = datetime.datetime.now()
        todo.save()
        return redirect("/")
         
    
class AddNewTodo(CreateView):
    model = Todo
    form_class = AddNewTodoForm
    success_url = '/'
    extra_context = {"form_status":"add"}

class TodoUpdateView(UpdateView):
    model = Todo
    form_class = AddNewTodoForm
    success_url = '/'
    extra_context = {"form_status":"update"}
    
    
    
# CRUD
 
    # View - http method lariga javob beruvchi ota controller class 
    
    
    
    # Create - yozish
    # Retrieve - oqish 
    # Update  - yangilash 
    # Delete  - ochirish
    
    

    # ListView
    # DetailView
    # TemplateView