from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {'author': 'Dr. Roya',
     'title': 'Post 1',
     'content': 'lorem ipsum 1',
     'date': 'Today'},
    {'author': 'Jane Doe',
     'title': 'Post 2',
     'content': 'lorem ipsum 2',
     'date': 'Today 2'}
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About Us'})
