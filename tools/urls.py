from django.conf.urls import *
from django.urls import path
from tools.views import *

urlpatterns = [
	path('', index),
]
