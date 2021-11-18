from .models import *

def view_all(request):
    context = {
        "categories":Category.objects.all(),
        "tags":Tag.objects.all()
    }
    return context