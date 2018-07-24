from django.contrib import admin
from blog.models import *


# Register your models here.


class BlogPostAdmin(admin.ModelAdmin):
	list_display = ['title', 'body', 'timestamp']


# admin.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogPost, BlogPostAdmin)

admin.site.register(DiaryPost, BlogPostAdmin)


class MediaAdmin(admin.ModelAdmin):
	list_display = ['username', 'img', 'video', 'time']


admin.site.register(Media, MediaAdmin)
