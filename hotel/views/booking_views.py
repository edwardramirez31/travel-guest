from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from hotel.serializers.booking_serializer import BookingSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class BookingModelViewSet(ModelViewSet):
    """
    A simple ViewSet created for our admin staff
    PERMISSIONS NEEDED
    """

    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return (
            self.get_serializer()
            .Meta.model.objects.all()
            .filter(user=self.request.user)
            .select_related("hotel")
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def put(self, request, *args, **kwargs):
        instance = Booking.objects.get()

        data = request.data

        instance.total_person = data["total_person"]
        instance.total_price = data["total_price"]
        instance.begining_date = data["begining_date"]
        instance.ending_date = data["ending_date"]

        instance.save()

        serializer = BookingSerializer(instance)
        return Reponse(serializer.data)

    def destroy(self, request, *args, **kwargs):
        logedin_user = request.user
        instance = self.get_object()
        instance.delete()
        response_message = {"mensaje": "La reserva ha sido eliminada"}
        return Response(response_message)

        # posible autentificación de reviews
        """
        if(IsAdminUser):
            instance = self.get_object()
            instance.delete()
            response_message ={"mensaje":"La reserva ha sido eliminada"}
        else:
            response_message = {"mensaje":"No tiene los permisos"}
        return Response(response_message)
        """


class BookingReadOnlyViewSet(ReadOnlyModelViewSet):
    """
    A simple ViewSet created for our users
    JUST READ ONLY
    """

    serializer_class = BookingSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
