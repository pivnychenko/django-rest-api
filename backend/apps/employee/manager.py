from django.db import models
from django.contrib.auth.models import BaseUserManager

class EmployeeManager(BaseUserManager):
    """
    custom registration manager
    """
    def create(self, phone_number, password=None, name=None, is_admin=False, *args, **kwargs):
        """
        create user Employee
        """
        if not phone_number:
            raise ValueError("Users must have an phone number")
        if not password:
            raise ValueError("Users must have a password")

        user_obj = self.model(
            name=name,
            phone_number=phone_number,
        )

        user_obj.set_password(password)
        user_obj.admin = is_admin
        user_obj.save()
        return user_obj

    def create_superuser(self, phone_number, password=None, *args, **kwargs):
        """
        create superuser Employee
        """
        user = self.create(
            phone_number,
            password=password,
            is_staff=True,
            is_admin=True,
            name=None
        )
        return user
