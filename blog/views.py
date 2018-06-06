from django.shortcuts import render, render_to_response
from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import BlogPost


# Create your views here.

def blog_index(request):
    blog_list = BlogPost.objects.all()[:5]
    # t = loader.get_template('index.html')
    # c: Context = Context({'blog_list': blog_list})
    # # return render(request, t, c)
    # # return HttpResponse(t.render(c))
    # return render(request, 'index.html', {'blog_list': blog_list})
    # replaced by the following
    return render_to_response('index.html', {'blog_list': blog_list})


archive = lambda req: render_to_response('index.html', {'blog_list': BlogPost.objects.all()[:5]})


def create_blog_post(request):
    if request.method == 'POST':
        BlogPost(
            title=request.POST.get('title'),
            body=request.POST.get('body'),
            timestamp=request.POST.get('timestamp'),
        ).save()
    return HttpResponseRedirect('/blog/')
