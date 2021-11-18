from django.shortcuts import render
from .models import *
# Create your views here.
def homeView(request):
    context = {
        "students":Student.objects.first(),
        "rooms":Room.objects.last(),
        "teachers":Teacher.objects.all()
    }
    return render(request, "index.html", context)