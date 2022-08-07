from django.contrib import admin
from .models.hotel import Hotel
from .models.review import Review
from .models.booking import Booking


class HotelAdmin(admin.ModelAdmin):
    list_per_page = 20


class ReviewAdmin(admin.ModelAdmin):
    list_per_page = 20

class BookingAdmin(admin.ModelAdmin):
    list_per_page = 20

admin.site.register(Hotel, HotelAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Booking, BookingAdmin)