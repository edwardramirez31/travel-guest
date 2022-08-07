from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from hotel.serializers.review_serializer import (
    ReviewSerializer,
    ReviewReadOnlySerializer,
)
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class ReviewModelViewSet(ModelViewSet):

    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()

    def put(self, request, *args, **kwargs):
        instance = Review.objects.get()

        data = request.data

        instance.total_person = data["total_person"]
        instance.total_price = data["total_price"]
        instance.begining_date = data["begining_date"]
        instance.ending_date = data["ending_date"]

        instance.save()

        serializer = ReviewSerializer(instance)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        logedin_user = request.user
        instance = self.get_object()
        instance.delete()
        response_message = {"mensaje": "La reserva ha sido eliminada"}
        return Response(response_message)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReviewReadOnlyViewSet(ReadOnlyModelViewSet):

    serializer_class = ReviewReadOnlySerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
