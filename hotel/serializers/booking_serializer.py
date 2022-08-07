from rest_framework import serializers
from hotel.models.booking import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["total_person", "hotel", "begining_date", "ending_date"]

    def to_representation(self, instance):
        return {
            "total_person": instance.total_person,
            "total_price": instance.total_price,
            "begining_date": instance.begining_date,
            "ending_date": instance.ending_date,
            "hotel": instance.hotel.name,
        }

    def create(self, validated_data):
        """This method is called each time the view calls serializer.save()"""
        booking = Booking(**validated_data)
        price = booking.hotel.price_per_people * booking.total_person
        booking.total_price = price
        booking.save()
        return booking
