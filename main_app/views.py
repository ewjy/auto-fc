from django.shortcuts import render
from django.contrib import admin

# Create your views here.
def index(request):
	return render(request, "index.html")
def learn(request):
    return render(request, "learn.html")
def about(request):
    return render(request, "about.html")