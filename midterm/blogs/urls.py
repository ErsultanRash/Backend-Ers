from django.urls import path
from .views import *

urlpatterns = [
    path('api/blogs', blogs_list, name='blogs_list'),
    path('api/blogs/<int:pk>', blog_detail, name='blog_detail'),
]
