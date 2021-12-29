from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class AdminUser(admin.ModelAdmin):
	fields = ('name', 'phone_number',)

	def get_fields(self, request, obj=None):
		if not obj:  # add an existing object
			return self.fields + ('password',)
		return self.fields