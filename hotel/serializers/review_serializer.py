from rest_framework import serializers
from hotel.models.review import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ["user", "created_at", "updated_at"]


class ReviewReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "score": instance.score,
            "opinion": instance.opinion,
            "created_at": instance.created_at,
            "updated_at": instance.updated_at,
            "userId": instance.user.id,
            "user": instance.user.username,
            "hotel": instance.hotel.id,
        }
