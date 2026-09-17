from django.urls import path
from . import views

urlpatterns = [
    path('event-tickets/', views.event_tickets_view, name='event-tickets'),
    path('event-ticket-details/<slug:slug>/', views.event_tickets_details_view, name='event-ticket-details'),
    path('payment/<uuid:uid>/', views.payment_process_view, name='payment-process'),
    path('payment-success/', views.payment_success_view, name='payment-success'),
    path('booking-confirmed/<uuid:uid>/', views.booking_confirmed_view, name='booking-confirmed'), 
]

