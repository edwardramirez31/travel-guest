from django.db import models
from .hotel import Hotel
from authapp.models.user import User


class Review(models.Model):
    """docstring for Review."""

    score = models.FloatField()
    opinion = models.TextField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="all_user_reviews"
    )
    hotel = models.ForeignKey(
        Hotel, on_delete=models.CASCADE, related_name="all_reviews"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.hotel} review by {self.user}"
