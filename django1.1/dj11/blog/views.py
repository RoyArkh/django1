from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Tag

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


# def search_tag(request, tag):
#     tag_obj = Tag.objects.filter(name=tag).first()

#     if tag_obj:
#         tagged_posts = Post.objects.filter(tags=tag_obj)
#         context = {
#             'posts': tagged_posts,
#             'tag': tag,
#         }
#     else:
#         context = {
#             'posts': [],
#             'tag': tag,
#         }

#     return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About Us'})


def search_tags(request, tags):
    tag_names = tags.split('_')
    tag_objs = Tag.objects.filter(name__in=tag_names)

    if tag_objs:
        tagged_posts = Post.objects.filter(tags__in=tag_objs).distinct()
        context = {
            'posts': tagged_posts,
            'tags': tag_names,
        }
    else:
        context = {
            'posts': [],
            'tags': tag_names,
        }

    return render(request, 'blog/home.html', context)

