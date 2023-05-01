from django.shortcuts import render,redirect
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, CustomUserCreationForm

# Create your views here.
def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(form.data["username"])
        user = authenticate(username=form.data['username'], password=form.data['password'])
        print(user)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            print("ERROR")
            return render(request, 'auth/login.html',{"form":form})
    return render(request, 'auth/login.html', {"form":form})

def my_register_view(request): 
    if request.method == 'POST': 
        form = CustomUserCreationForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect("/")
    else: 
        form = CustomUserCreationForm() 
    context = { 
        'form':form 
    } 
    return render(request, 'auth/register.html', context) 

def logged_out(request):
    logout(request)
    return redirect("/accounts/login/")