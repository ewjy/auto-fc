from django.shortcuts import render
from django.contrib import admin
from .models import Factcheck
# Create your views here.
def index(request):
	data = Factcheck.objects.all()
	context = {
			'data' : data.Title,
			'website' : data.Website,
	}
	return render(request, "index.html")
def learn(request):
    return render(request, "learn.html")
def about(request):
    return render(request, "about.html")