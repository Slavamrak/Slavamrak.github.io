from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class BuildAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'time_create', 'photo', 'photoTi')
	search_fields = ('title', 'content')
	list_filter = ('time_create',)

	def get_html_photo(self, object):
		if object.photo:
			return mark_safe(f"<img src='{object.photo.url}' width=50>")

admin.site.register(Build, BuildAdmin)

class SaleAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'time_create', 'photo')
	search_fields = ('title', 'content')
	list_filter = ('time_create',)

admin.site.register(Sale, SaleAdmin)