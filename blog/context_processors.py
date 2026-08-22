from django.http import request
from .models import Category
from aboutUs.models import SocialLink

def get_context(request):
    categories = Category.objects.all()
    return dict(categories=categories)

def get_social_link(request):
    links = SocialLink.objects.all()
    return dict(links = links)