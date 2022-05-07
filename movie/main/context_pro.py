from .models import *

def view_all(request):
    context = {
        'categories':Category.objects.all(),
        'genres':Genre.objects.all(),
    }
    return context