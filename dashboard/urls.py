from django.urls import path
from . import views

urlpatterns = [
    path("",views.dashboard,name='dashboard'),
    path("categories/",views.categories,name='categories'),
    path("categories/add/",views.add_category,name='add_category'),
    path("categories/edit/<int:category_id>/",views.edit_category,name='edit_category'),
    path("categories/delete/<int:category_id>/",views.delete_category,name='delete_category'),
    path("post/",views.post,name='blog_post'),
    path("post/add/",views.add_blog,name='add_blog'),
    path("post/edit/<int:pk>/",views.edit_blog,name='edit_blog'),
    path("post/delete/<int:pk>/",views.delete_blog,name='delete_blog'),
    path("users/",views.users , name='users'),
    path("users/add/",views.add_user,name='add_user'),
    path("users/edit/<int:pk>/",views.edit_user,name='edit_user'),
    path("users/delete/<int:pk>/",views.delete_user,name='delete_user'),
    

]
