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
        null=True,
        blank=True,  # needed for django admin
        default=None,
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

    def __str__(self):
        return f'Employee - {self.name}'

    class Meta:
        verbose_name = "User - Employee"
        verbose_name_plural = "User - Employee"
