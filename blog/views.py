from django.shortcuts import render, render_to_response
from django.template import loader, Context
from django.http import HttpResponse
from blog.models import BlogPost


# Create your views here.

def blog_index(request):
    blog_list = BlogPost.objects.all()
    # t = loader.get_template('index.html')
    # c: Context = Context({'blog_list': blog_list})
    # # return render(request, t, c)
    # # return HttpResponse(t.render(c))
    # return render(request, 'index.html', {'blog_list': blog_list})
    return render_to_response('index.html',  {'blog_list': blog_list})