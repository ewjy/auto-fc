from django.shortcuts import render
from django.contrib import admin
from .models import Factcheck
# Create your views here.
def index(request):
	data = Factcheck.objects.all()
	return render(request, "index.html")
def learn(request):
    return render(request, "learn.html")
def about(request):
    return render(request, "about.html")
def results_title(request):
	return render(request, "results_title.html")
def results_url(request):
	return render(request, "results_url.html")