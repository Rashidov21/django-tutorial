from django.shortcuts import render

# Create your views here.


def homePageView(request):
    return render(request,"index.html")
def qurutsPageView(request):
    return render(request,"quruts.html")