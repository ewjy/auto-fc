from django.contrib import admin
from .models import Factcheck
# Register your models here.
class DataAdmin(admin.ModelAdmin):
	data_display = ('title', 'pref')
	
admin.site.register(Factcheck,DataAdmin)