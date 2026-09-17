from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify
import uuid
class EventDetails(models.Model):
    subtitle = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    event_banner = models.ImageField(upload_to="event")

    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    venue = models.CharField(max_length=200)
    address = models.TextField()
    organizer = models.CharField(max_length=200)
    map_url = models.URLField(max_length=500, blank=True, null=True) 

    description = HTMLField(blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    class Meta:
        db_table="event_details"
        verbose_name="Event Details"
        verbose_name_plural="Event Details"


class UserDetails(models.Model):
    # Order Status Choices
    STATUS_PENDING = 'PENDING'
    STATUS_SUCCESS = 'SUCCESS'
    STATUS_FAILED = 'FAILED'
    STATUS_REFUNDED = 'REFUNDED'

    ORDER_STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_SUCCESS, 'Success / Paid'),
        (STATUS_FAILED, 'Failed'),
        (STATUS_REFUNDED, 'Refunded'),
    ]

    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    # Event & User Information
    event_details = models.ForeignKey(EventDetails, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    organization =models.CharField(max_length=50,blank=True)
    quantity = models.PositiveIntegerField(default=1)

    # Razorpay Transaction Identifiers
    razorpay_order_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
# Status Tracking
    order_status = models.CharField(
        max_length=20, 
        choices=ORDER_STATUS_CHOICES, 
        default=STATUS_PENDING
    )
    is_paid = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True)
    email_sent = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name} - {self.order_status} ({self.uid})"
    
    class Meta:
        db_table="user_details"
        verbose_name="User Details"
        verbose_name_plural="User Details"
    

    

 