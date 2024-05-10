from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('filter/<str:tag>/', views.search_tag, name='blog-tagged'),
    path('filter/', views.home, name='blog-home'),
]

