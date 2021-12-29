from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from .manager import EmployeeManager
from apps.validations import PHONE_NUMBER_REGEX


class Employee(AbstractBaseUser):
    """
    User Employee from EmployeeManager
    """
    name = models.CharField(
        verbose_name="Name Worker",
        max_length=200)

    phone_number = models.CharField(
        verbose_name="Phone Number",
        max_length=15,
        unique=True,
        validators=[PHONE_NUMBER_REGEX])

    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'

    # Settings
    objects = EmployeeManager()

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        return True

    @property
    def is_admin(self):
        return self.admin

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "User - Employee"
        verbose_name_plural = "User - Employee"
