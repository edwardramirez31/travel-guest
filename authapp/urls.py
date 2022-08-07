from django.urls import path

from knox.views import LogoutView
from rest_framework.routers import SimpleRouter

from .views.user_views import (
    ChangePasswordUpdateAPIView,
    LoginView,
    RegisterView,
    UserModelViewSet,
    UserDestoyAPIView,
    UserUpdateAPIView,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="knox_logout"),
    path(
        "update-password/",
        ChangePasswordUpdateAPIView.as_view(),
        name="update_password_api",
    ),
    path("delete-user/<int:pk>/", UserDestoyAPIView.as_view(), name="user_delete"),
    path("update-user/<int:pk>/", UserUpdateAPIView.as_view(), name="user_update"),
]

router = SimpleRouter()
router.register("user", UserModelViewSet, basename="user")

urlpatterns += router.urls
