from django.db import models
from .hotel import Hotel
from authapp.models.user import User
from django.utils.translation import gettext_lazy as _


class Booking(models.Model):
    total_person = models.IntegerField()
    total_price = models.FloatField()
    begining_date = models.DateField()
    ending_date = models.DateField()

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="all_bookings"
    )
    hotel = models.ForeignKey(
        Hotel, on_delete=models.CASCADE, related_name="all_bookings"
    )

    class Meta:
        verbose_name = _("Booking")
        verbose_name_plural = _("Bookings")

    def __str__(self):
        return f"{self.hotel} reservado por {self.user}"
