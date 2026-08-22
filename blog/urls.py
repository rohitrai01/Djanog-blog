from django.urls import path
from . import views

urlpatterns = [
    path("<int:category_id>/",views.category_post,name='post_by_category')
]
