from django.contrib.auth import get_user_model

from knox.models import AuthToken
from rest_framework import status
from rest_framework.generics import DestroyAPIView, GenericAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from authapp.serializers.user_serializer import (
    ChangePasswordSerializer,
    LoginSerializer,
    RegisterSerializer,
    UserSerializer,
)


class UserModelViewSet(ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()


class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        register_serializer = self.get_serializer(data=request.data)
        register_serializer.is_valid(raise_exception=True)
        user = register_serializer.save()
        instance, token = AuthToken.objects.create(user)
        message = {
            "user": UserSerializer(user).data,
            "token": token,
            "expiry": instance.expiry.strftime("%d %b %Y %H:%M:%S"),
        }
        return Response(message, status=status.HTTP_201_CREATED)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        login_serializer = self.get_serializer(data=request.data)
        login_serializer.is_valid(raise_exception=True)
        user = login_serializer.validated_data["user"]
        instance, token = AuthToken.objects.create(user)
        message = {
            "user": UserSerializer(user).data,
            "token": token,
            "expiry": instance.expiry.strftime("%d %b %Y %H:%M:%S"),
        }

        return Response(message, status=status.HTTP_200_OK)


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


class UserDestoyAPIView(DestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()


class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
