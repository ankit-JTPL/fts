from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_views, name='home'),
    path('agenda/', views.agenda_views, name='agenda'),
    path('speakers/', views.speakers_views, name='speakers'),
    path('sponsors/', views.sponsors_views, name='sponsors'),
    path('media/', views.media_views, name='media'),
    path('contact/', views.contact_views, name='contact'),
    path('thank-you/', views.thankyou_views, name='thank-you'),
   

    path('terms-and-conditions/', views.tnc, name='tnc'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('refund-policy/', views.refund_policy, name='refund_policy'),
  
    
]
