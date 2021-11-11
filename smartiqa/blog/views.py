from django.shortcuts import render
from .models import  Tag
# from django.views.generic.base import (
# TemplateView, View
# )
# Create your views here.

# class HomeView(TemplateView):
#     template_name = "index.html"
def homeView(request):
    tags = Tag.objects.all()
    return render(request, "index.html" , {"tags":tags})


