from django.forms import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Tag
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


#app/model_viewtype.html
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

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

