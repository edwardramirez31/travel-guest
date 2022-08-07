from rest_framework import generics

from authapp.models.user import User
from authapp.serializers.user_serializer import UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
