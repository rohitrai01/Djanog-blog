from django.shortcuts import render,redirect
from django.http import request
from blog.models import Category,Blog
from aboutUs.models import About
from .forms import RegistrationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    categories = Category.objects.all()
    featured = Blog.objects.filter(is_featured=True,status='Published').order_by('created_at')
    posts = Blog.objects.filter(is_featured = False,status ='Published')
    try:
        about = About.objects.get()
    except:
        about=None
    context = {
        'categories':categories,
        'featured':featured,
        'posts' : posts,
        'about':about
    }
    return render(request,'home.html',context)

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form = RegistrationForm()
    context={
        'form':form
    }
    return render(request,'register.html',context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=="POST":
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()

    context={
        'form':form
    }
    return render(request , 'login.html',context)

def logout_view(request):
    logout(request)
    return redirect('home')