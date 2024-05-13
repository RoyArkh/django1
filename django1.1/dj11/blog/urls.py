from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('filter/<str:tags>/', views.search_tags, name='search-tags'),
    path('filter/', views.home, name='blog-home'),
]

