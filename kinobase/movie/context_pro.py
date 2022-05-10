from .models import Category
# from django.contrib.auth.models import User
def view_all(request):
    context = {
        "categories":Category.objects.all()
    }
    
    return context  