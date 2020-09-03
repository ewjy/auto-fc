from django.shortcuts import render
from django.contrib import admin
from .models import Factcheck
import whois
from urllib.parse import urlparse
from nslookup import Nslookup
import ipinfo
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
		'query' : query,
		'result' : query_list,
	}
	return render(request, "results_title.html",context)
def results_url(request):
    if 'href' in request.GET:
        href = request.GET['href']
        domain = urlparse(href).netloc
        data = whois.whois(domain)
        dns_query = Nslookup(dns_servers = ["1.1.1.1"])
        ips_record = dns_query.dns_lookup(domain)
        ip_record = ips_record.answer[0]
        access_token = 'efd54bc59b7a42' # For IP info query
        handler = ipinfo.getHandler(access_token)
        ip_address = ip_record
        details = handler.getDetails(ip_address)
        ip_country = details.country_name
        ip_org = details.org
    context = {
        'data' : data,
        'ip_record' : ip_record,
        'ip_country' : ip_country,
        'ip_org' : ip_org,
    }
    return render(request, "results_url.html",context)