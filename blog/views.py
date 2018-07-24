from django.shortcuts import render, render_to_response
from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from blog.models import BlogPost, blogPostToForm, UserForm, Media
from datetime import datetime
from django.http import StreamingHttpResponse
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


def file_down(request):
	file = open('collected_static/bm.mp4', 'rb')
	response = FileResponse(file)
	response['Content-Type'] = 'application/octet-stream'
	response['Content-Disposition'] = 'attachment;filename="bm.mp4"'
	return response


def upload(request):
	if request.method == 'POST':
		form = UserForm(request.POST, request.FILES)
		if form.is_valid():
			# username = form.cleaned_data['user_name']
			# head_img = form.cleaned_data['headImg']
			Media(
				username=request.POST.get('username'),
				img=request.FILES.get('img'),
				video=request.FILES.get('video'),
				# django 里面上传文件默认只处理单个文件上传，批量上传的时候request.FILES 的类型
				# 为 MultiValueDict，这种字典类是特殊定义的，要取得list 需要调用 getlist方法:
				time=datetime.now()
			).save()
			
			return HttpResponseRedirect('/blog/upload')
	else:
		form = UserForm()
	return render(request, "register.html", {'form': form})

# def load_file(request):
# if request.method = ''

# def download(request):
# 	def file_iterator(file_name, chunk_size=512):
# 		with open(file_name) as f:
# 			while True:
# 				c = f.read(chunk_size)
# 				if c:
# 					yield c
# 				else:
# 					break
#
# 	filename = 'bm.mp4'
# 	response = StreamingHttpResponse(file_iterator(filename))
# 	response['Content-Type'] = 'application/octet-stream'
# 	response['Content-Disposition'] = 'attachment;filename="{0}"'.format((filename))
# 	return response
