import json
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView,DetailView
from django.http import JsonResponse
from .models import Post, Category
# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = "index.html"
    
class PostDetailView(DetailView):
    model = Post

def category_list(request, category_slug):
    category = Category.objects.get(slug=category_slug) #javascript
    posts = Post.objects.filter(category=category)
    paginator = Paginator(posts, 2) # Show 2 posts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "blog/post_list.html",{"page_obj":page_obj})
# views  


def inlineSearch(request):
    d = json.loads(request.GET.get("data"))
    queryset = list(Post.objects.filter(title__icontains=d).values())
    data = {}
    data["object_list"] = queryset

    return JsonResponse(data)