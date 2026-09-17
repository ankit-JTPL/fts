from django.contrib import admin
from apps.core.models import Contact

@admin.register(Contact)
class ContactDetails(admin.ModelAdmin):
    list_display = (
        "id",
        "interest",
        "full_name",
        "position",
        "company",
        "email",
        "phone",
        "message",
        "marketing_consent",
        "created_at",  
    )