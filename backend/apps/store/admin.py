from django.contrib import admin
from .models import Store, Visit

admin.site.register(Store)

@admin.register(Visit)
class AdminUser(admin.ModelAdmin):
	fields = ('last_visit', 'store', 'lat', 'long',)
	readonly_fields = ('last_visit', 'store', 'lat', 'long',)

	def has_add_permission(self, request, obj=None):
		return False

	def has_change_permission(self, request, obj=None):
		return False

	def has_delete_permission(self, request, obj=None):
		return False