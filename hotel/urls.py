from rest_framework.routers import SimpleRouter
from .views.hotel_views import HotelModelViewSet, HotelReadOnlyViewSet 
from .views.booking_views import BookingModelViewSet, BookingReadOnlyViewSet
from .views.review_views import ReviewModelViewSet, ReviewReadOnlyViewSet

urlpatterns = []

router = SimpleRouter()
router.register("hotel-admin", HotelModelViewSet, basename="hotel-admin")
router.register("hotel", HotelReadOnlyViewSet, basename="hotel")
router.register("booking-user", BookingModelViewSet, basename="booking-user")
router.register("booking", BookingReadOnlyViewSet, basename="booking")
router.register("review-user", ReviewModelViewSet , basename="review-user")
router.register("review", ReviewReadOnlyViewSet, basename="review")
urlpatterns += router.urls
