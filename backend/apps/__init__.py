from django.apps import AppConfig


class EmployeeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "apps.employee"


class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "apps.store"
