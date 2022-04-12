import json
from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.generic import ListView,DetailView
from django.http import JsonResponse, HttpResponse
from .models import Post, Category, Comment
# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = "index.html"
    
# class PostDetailView(DetailView):
#     model = Post

def post_detail(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    # print(request.path)
    # print(request.method)
    # print(request.get_host())
    # print(request.get_port())
    if request.method == "POST":
        # print(request.POST["name"])
        # print(request.POST["message"])
        name = request.POST.get("name")
        message = request.POST.get("message")
        if name and message:
            Comment.objects.create(
                post=post,
                name=name,
                message=message
            )
            messages.add_message(request, messages.SUCCESS, "Successfully !")
        else:
            messages.add_message(request, messages.WARNING, "Error !")
    else:
        print("Error")
    
    
    return render(request, 'blog/post_detail.html',{"post": post})

def category_list(request, category_slug):
    category = Category.objects.get(slug=category_slug) #javascript
    posts = Post.objects.filter(category=category)
    paginator = Paginator(posts, 2) # Show 2 posts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "blog/post_list.html",{"page_obj":page_obj})
# views  

def comments(request):
    return HttpResponse("Request") 

def inlineSearch(request):
    d = json.loads(request.GET.get("data"))
    queryset = list(Post.objects.filter(title__icontains=d).values())
    data = {}
    data["object_list"] = queryset

    return JsonResponse(data)

def likePost(request):  
    res = {}
    data = json.loads(request.GET.get('data'))
    post_id = data["post_id"]
    post = Post.objects.get(id=post_id)
    if post:
        post.rating += 1
        post.save()
        res["success"] = 200
        res["likes"] = post.rating
    else:
        res["error"] = 404
        res["likes"] = post.rating
    
    return JsonResponse(res)