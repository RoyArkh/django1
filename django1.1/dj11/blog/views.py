from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def tagged_posts(request, tag):
    posts = Post.objects.filter(tags__name=tag)
    context = {
        'posts': posts,
        'tag': tag  # Pass the tag to the template for display or further processing
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About Us'})
