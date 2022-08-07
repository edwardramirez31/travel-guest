from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authapp.serializers.user_serializer import (
    ChangePasswordSerializer,
    UserSerializer,
)


class ChangePasswordUpdateAPIView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = get_user_model()
    permission_classes = [IsAuthenticated]

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.obj = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.obj.check_password(serializer.data.get("old_password")):
                return Response(
                    {"message": "Wrong Password"}, status=status.HTTP_400_BAD_REQUEST
                )

            self.obj.set_password(serializer.data.get("new_password"))
            self.obj.save()
            message = {
                "status": "success",
                "message": "Password updated successfully",
            }
            return Response(message, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
