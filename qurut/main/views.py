from django.shortcuts import render

# Create your views here.
from .models import Category, Product

def homePageView(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    data = {
        "products":products,
        "categories":categories
    }
    
    return render(request,"index.html", context=data)

def qurutsPageView(request):
    return render(request,"quruts.html")