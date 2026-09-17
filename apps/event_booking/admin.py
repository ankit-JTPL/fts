from django.contrib import admin
from apps.event_booking.models import EventDetails, UserDetails

@admin.register(EventDetails)
class EventDetailsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "subtitle",
        "title",
        "price",
        "event_banner",
        "start_date",
        "end_date",
        "start_time",
        "end_time",
        "venue",
        "address",
        "organizer",
        "map_url",
        "description",
        "is_active",
    )

@admin.register(UserDetails)
class EventDetailsAdmin(admin.ModelAdmin):
    list_display = (
            "uid",
            "event_details",
            "full_name",
            "email",
            "phone",
            "organization",
            "quantity",
            "is_paid"
        )
    