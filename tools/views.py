from django.shortcuts import render
from tools.models import AddForm
from django.http import HttpResponse


# Create your views here.

def index(request):
	if request.method == 'POST':
		form = AddForm(request.POST)
		if form.is_valid():
			a = form.cleaned_data['a']
			b = form.cleaned_data['b']
			return HttpResponse(str(int(a) + int(b)))
	else:
		form = AddForm()
	return render(request, 'tools/algebra.html', {'form': form})
