from django.shortcuts import render
from .models import Students

# Create your views here.
def home(request):
    all_students = Students.objects.all()
    # for i in all_students:
    #     print(type(i))
    context = {
        "students":all_students,
        "test":"Python Django"
    }
    return render(request, "home.html", context)
