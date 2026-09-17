import razorpay
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from django.contrib import messages
from razorpay.errors import SignatureVerificationError

from apps.event_booking.models import EventDetails, UserDetails
from apps.event_booking.utils import send_ticket_email  


def event_tickets_view(request):
    events_data = EventDetails.objects.filter(is_active=True)
    return render(request, "event_booking/event-tickets.html", {"events_data": events_data})


def event_tickets_details_view(request, slug):
    event_details = get_object_or_404(EventDetails, slug=slug, is_active=True)
    
    if request.method == "POST":
        full_name = request.POST.get('full_name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        organization = request.POST.get('organization', '').strip()
        quantity = int(request.POST.get("quantity", 1))

        # 1. Save Initial Booking with PENDING status
        user_details = UserDetails.objects.create(
            event_details=event_details,
            full_name=full_name,
            email=email,
            phone=phone,
            organization=organization,
            quantity=quantity,
            order_status=UserDetails.STATUS_PENDING,
            is_paid=False
        )
        
        # 2. Redirect to Payment Gateway using UID
        return redirect("payment-process", uid=user_details.uid)

    return render(request, "event_booking/event-ticket-details.html", {"event_details": event_details})


def payment_process_view(request, uid):
    user_details = get_object_or_404(UserDetails, uid=uid)
    
    # Check if already paid to prevent double charge
    if user_details.is_paid or user_details.order_status == UserDetails.STATUS_SUCCESS:
        messages.info(request, "This booking has already been completed.")
        return redirect("event-tickets")
    
    total_price = user_details.event_details.price * user_details.quantity
    amount_in_paise = int(total_price * 100)

    key_id = str(settings.RAZORPAY_KEY_ID).strip()
    key_secret = str(settings.RAZORPAY_KEY_SECRET).strip()

    client = razorpay.Client(auth=(key_id, key_secret))
    try:
        # Create Razorpay Order
        razorpay_order = client.order.create({
            "amount": amount_in_paise,
            "currency": "INR",
            "receipt": f"order_{str(user_details.uid)[:20]}",
            "payment_capture": "1"
        })
        user_details.razorpay_order_id = razorpay_order['id']
        user_details.save()

    except Exception as e:
        messages.error(request, "Failed to create payment order. Please try again.")
        return redirect("event-tickets")

    context = {
        "user_details": user_details,
        "order_id": razorpay_order['id'],
        "razorpay_key": key_id,
        "amount": total_price,
        "amount_in_paise": amount_in_paise,
    }
    print(amount_in_paise)
    return render(request, "event_booking/payment.html", context)


# apps/event_booking/views.py

@csrf_exempt
def payment_success_view(request):
    if request.method == "POST":
        payment_id = request.POST.get('razorpay_payment_id')
        order_id = request.POST.get('razorpay_order_id')
        signature = request.POST.get('razorpay_signature')

        params_dict = {
            'razorpay_order_id': order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        }

        key_id = str(settings.RAZORPAY_KEY_ID).strip()
        key_secret = str(settings.RAZORPAY_KEY_SECRET).strip()
        client = razorpay.Client(auth=(key_id, key_secret))

        try:
            # 1. Verify Signature  
            client.utility.verify_payment_signature(params_dict)

            # 2. Fetch Database Record
            user_details = UserDetails.objects.get(razorpay_order_id=order_id)

            # 3. Status & Email Check (Only send once)
            if not user_details.is_paid:
                user_details.order_status = UserDetails.STATUS_SUCCESS
                user_details.is_paid = True
                user_details.razorpay_payment_id = payment_id
                # Check email sent flag
                if not user_details.email_sent:
                    send_ticket_email(user_details)
                    user_details.email_sent = True
                user_details.save()

            return redirect("booking-confirmed", uid=user_details.uid)

        except SignatureVerificationError:
            messages.error(request, "Payment verification failed. Invalid Signature.")
            return redirect("event-tickets")

        except UserDetails.DoesNotExist:
            return HttpResponseBadRequest("Order record not found.")
    return HttpResponseBadRequest("Invalid Request Method")


def booking_confirmed_view(request, uid):
    user_details = get_object_or_404(UserDetails, uid=uid)
    return render(request, "event_booking/payment-success.html", {
        "user_details": user_details,
        "payment_id": user_details.razorpay_payment_id,
        "order_id": user_details.razorpay_order_id
    })