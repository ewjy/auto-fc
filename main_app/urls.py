from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index, name = "index"),
    path('about/',views.about, name = 'about'),
    path('learn/',views.learn, name = 'learn'),
    path('results_title/',views.results_title, name = 'results_title'),
    path('results_url/',views.results_url, name = 'results_url'),
]