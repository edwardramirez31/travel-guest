from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from hotel.serializers.hotel_serializer import HotelSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from hotel.serializers.review_serializer import (
    ReviewReadOnlySerializer,
)


class HotelModelViewSet(ModelViewSet):
    """
    A simple ViewSet created for our admin staff
    PERMISSIONS NEEDED
    """

    serializer_class = HotelSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()


class HotelReadOnlyViewSet(ReadOnlyModelViewSet):
    """
    A simple ViewSet created for our users
    JUST READ ONLY
    """

    serializer_class = HotelSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        hotel_reviews = instance.all_reviews.all().order_by("-updated_at")
        reviews = ReviewReadOnlySerializer(hotel_reviews, many=True)
        data = {"hotel": serializer.data, "reviews": reviews.data}
        return Response(data)
