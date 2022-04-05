from django.shortcuts import render
from .models import Post
# Create your views here.


def homeView(request):
    posts = Post.objects.all()
    # for post in posts:
    #     print(dir(post))
    # print(dir(posts))
    # print(type(posts))
    context = {
        "posts":posts,
    }
    return render(request,"blog-home.html", context)
