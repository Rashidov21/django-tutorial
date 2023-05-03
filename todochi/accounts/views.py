from django.shortcuts import render,redirect
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, CustomUserCreationForm
from django.contrib.auth.models import User
from django.views.generic import View, UpdateView
from django import forms
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Profile

# Standart Auth views from Django 


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
            u = form.save(commit=False)
            Profile.objects.create(user=u)
            u.save() 
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

class ProfileView(LoginRequiredMixin,View):
    template_name = 'auth/profile.html'
    
    
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name, {"object":request.user})
        else:
            return redirect('accounts:login')



class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['birthday', 'image', 'bio']
        widgets = {
            'birthday':forms.DateInput()
        }
    
         
        
class ProfileUpdateView(UpdateView):
    model = Profile 
    form_class = ProfileUpdateForm
    template_name = 'auth/profile_form.html'
    success_url = reverse_lazy("accounts:profile")


