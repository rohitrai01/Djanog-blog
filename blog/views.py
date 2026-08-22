from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Blog,Category,Comment
from django.db.models import Q


def category_post(request,category_id):
    posts = Blog.objects.filter(category=category_id)
    
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')

    context = {
        'posts':posts,
        'category' : category
    }
    return render(request,'posts_by_category.html',context )

def blogs(request,slug):
    blog_obj = get_object_or_404(Blog , slug=slug)
    if request.method=="POST":
        comment=Comment()
        comment.name = request.user
        comment.blog = blog_obj
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)
    
    comments = Comment.objects.filter(blog=blog_obj)
    count = comments.count()
    context={
        'blog_obj':blog_obj,
        'comments':comments,
        'count':count
    }

    return render(request,'blogs.html',context)


def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword),status='Published')
    context={
        'keyword':keyword,
        'blogs':blogs
    }
    return render(request,'search.html',context)