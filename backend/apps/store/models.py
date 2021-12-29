from django.db import models
from django.urls import reverse
from django.utils import timezone

from apps.employee.models import Employee


class Store(models.Model):
    title = models.CharField(
        verbose_name="Title Store",
        max_length=300)

    user = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        verbose_name="Employee",
        related_name="user_workers")

    def get_absolute_url(self):
        return reverse('store_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Store"
        verbose_name_plural = "Store"


class Visit(models.Model):

    ip = models.GenericIPAddressField(
        verbose_name="IP address Visit Store",
        blank=True,
        null=True,
        default=None)

    last_visit = models.DateTimeField(
        verbose_name="Last Visit Store",
        default=timezone.now,
        null=True, blank=True)

    # best practices use PointField for lat and long
    lat = models.CharField(
        verbose_name="latitude Visit",
        max_length=300)

    long = models.CharField(
        verbose_name="longitude Visit",
        max_length=300)

    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        verbose_name="Visit Store")

    def set_visit_store(self, store, ip: str, data: dict):
        """
        method for visit store
        Args:
            data: Data lat long from GeoLocation
            store: Object store for visit

        Returns:
            Nothing.
        """

        if data:
            self.ip = ip
            self.lat = data.get("lat")
            self.long = data.get("long")
            self.store = store
            self.save()

    class Meta:
        verbose_name = "Store - Visit"
        verbose_name_plural = "Store - Visit"