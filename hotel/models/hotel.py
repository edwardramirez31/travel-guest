from django.db import models
from django.utils.translation import gettext_lazy as _


class Hotel(models.Model):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5

    STAR_CHOICES = [
        (ONE, "Una estrella"),
        (TWO, "Dos estrellas"),
        (THREE, "Tres estrellas"),
        (FOUR, "Cuatro estrellas"),
        (FIVE, "Cinco estrellas"),
    ]
    name = models.CharField(_("Name of Hotel"), max_length=45)
    city = models.CharField(_("City of Hotel"), max_length=45)
    address = models.CharField(_("Address of Hotel"), max_length=45)
    stars = models.IntegerField(_("Stars of Hotel"), choices=STAR_CHOICES)
    price_per_people = models.FloatField(default=0)
    picture = models.CharField(
        _("Hotel picture"),
        max_length=250,
        default="https://media-cdn.tripadvisor.com/media/photo-s/16/1a/ea/54/hotel-presidente-4s.jpg",
    )

    def __str__(self) -> str:
        return self.name
