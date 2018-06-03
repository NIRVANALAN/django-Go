from django.shortcuts import render
from blog.models import BlogPost


# Create your views here.

def blog_index(request):
    blog_list = BlogPost.objects.all()
    return render(request, 'index.html', {'blog_list': blog_list})
