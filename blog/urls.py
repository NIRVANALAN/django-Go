from django.conf.urls import *
from blog.views import *
from django.urls import path

urlpatterns = [
    path('', blog_index),
]
