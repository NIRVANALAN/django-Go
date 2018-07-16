from django.shortcuts import render, render_to_response
from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import BlogPost, blogPostToForm
from datetime import datetime
from django.views.generic import TemplateView

# Create your views here.

def blog_index(request):
    blog_list = BlogPost.objects.all()[:5]
    return render(request, 'index.html', {'blog_list': blog_list, 'form': blogPostToForm})

# archive = lambda req: render_to_response('index.html', {'blog_list': BlogPost.objects.all()[:5]})


def create_blog_post(request):
    if request.method == 'POST':
        BlogPost(
            title=request.POST.get('title'),
            body=request.POST.get('body'),
            timestamp=datetime.now(),
        ).save()
    return HttpResponseRedirect('/blog/')
