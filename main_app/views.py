from django.shortcuts import render
from django.contrib import admin
from .models import Factcheck
# Create your views here.
def index(request):
	return render(request, "index.html")
def learn(request):
    return render(request, "learn.html")
def about(request):
    return render(request, "about.html")
def results_title(request):
	query_list = Factcheck.objects.order_by('-title')
	if 'query' in request.GET:
		query = request.GET['query']
		if query:
			query_list = query_list.filter(title__icontains = query)
	context = {
		'result' : query_list
	}
	return render(request, "results_title.html",context)
def results_url(request):
	return render(request, "results_url.html")