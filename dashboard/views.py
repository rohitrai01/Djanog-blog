from django.shortcuts import render,redirect,get_object_or_404
from blog.models import Blog,Category
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm,BlogForm,AddUserForm,EditUserForm
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    category_count=Category.objects.all().count()
    post_count = Blog.objects.all().count()

    context={
        'category_count':category_count,
        'post_count':post_count
    }
    return render(request,'Dashboard/dashboard.html',context)

def categories(request):
    return render(request,'Dashboard/category.html')

def add_category(request):
    if request.method=="POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form=CategoryForm()
    context={
        'form':form
    }
    return render(request,'Dashboard/add_category.html',context)

def edit_category(request,category_id):
    cat_object = get_object_or_404(Category,pk=category_id)
    if request.method=="POST":
        form = CategoryForm(request.POST,instance=cat_object)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=cat_object)
    context ={
        'form':form,
        'category':cat_object
        }
    return render(request,'Dashboard/edit_category.html',context)

def delete_category(request,category_id):
    cat_obj = Category.objects.get(pk=category_id)
    cat_obj.delete()
    return redirect('categories')

def post(request):
    blogs = Blog.objects.all()
    context = {
        'blogs':blogs
    }
    return render(request,'Dashboard/post.html',context)


def add_blog(request):
    if request.method =="POST":
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            title = form.cleaned_data['title']
            post.slug=slugify(title)+'-'+ str(post.id)
            form.save()
            return redirect('blog_post')
    else:
        form = BlogForm()
    context= {
        'form':form
        }
    return render(request,'Dashboard/add_blog.html',context)

def edit_blog(request,pk):
    blog = Blog.objects.get(pk=pk)
    if request.method=="POST":
        form = BlogForm(request.POST,instance=blog)
        if form.is_valid():
            form.save()
            title = form.cleaned_data['title']
            blog.slug = slugify(title)+'-'+str(blog.id)
            form.save()
            return redirect('blog_post')
    else:
        form = BlogForm(instance=blog)
    context = {
        'form':form,
        'blog':blog
    }
    return render(request,'Dashboard/edit_blog.html',context)

def delete_blog(request,pk):
    blog=Blog.objects.get(pk=pk)
    blog.delete()
    return redirect('blog_post')

def users(request):
    users = User.objects.all()
    context={
        'users':users
    }
    return render(request,'Dashboard/user.html',context)

def add_user(request):
    if request.method=="POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        
    form = AddUserForm()
    context={
        'form':form
    }
    return render(request,'Dashboard/add_user.html',context)

def edit_user(request,pk):
    user_obj = User.objects.get(pk=pk)
    if request.method == "POST":
        form = EditUserForm(request.POST,instance=user_obj)
        if form.is_valid():
            form.save()
            return redirect('users')
    form = EditUserForm(instance=user_obj)
    context = {
        'form':form,
        'user_obj':user_obj
    }
    return render(request,'Dashboard/edit_user.html',context)

def delete_user(request,pk):
    user_obj = User.objects.get(pk=pk)
    user_obj.delete()
    return redirect('users')

    