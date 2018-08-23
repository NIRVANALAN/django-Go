from django.db import models
from django import forms


# Create your models here.

class AddForm(forms.Form):
	a = forms.IntegerField()
	b = forms.IntegerField()
