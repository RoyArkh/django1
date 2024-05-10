from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Tag

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def search_tag(request, tag):
    tag_obj = Tag.objects.filter(name=tag).first()

    if tag_obj:
        tagged_posts = Post.objects.filter(tags=tag_obj)
        context = {
            'posts': tagged_posts,
            'tag': tag,
        }
    else:
        context = {
            'posts': [],
            'tag': tag,
        }

    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About Us'})
