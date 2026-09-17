from django.shortcuts import render, redirect, get_object_or_404
from .models import  Contact
from django.contrib import messages



def home_views(request):
    return render(request, 'core/home.html')

def agenda_views(request):
    return render(request, 'core/agenda.html')

def speakers_views(request):
    return render(request, 'core/speakers.html')

def sponsors_views(request):
    return render(request, 'core/sponsors.html')

def media_views(request):
    return render(request, "core/media.html")




def contact_views(request):
    if request.method == "POST":
        interest = request.POST.getlist("interest")
        full_name = request.POST.get("full_name")
        position = request.POST.get("position")
        company = request.POST.get("company")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        marketing_consent = request.POST.get("marketing_consent") == "on"

        if Contact.objects.filter(email=email).exists():
            messages.error(request, "This email is already registered.")
            return redirect('contact')

        Contact.objects.create(
            interest=interest,
            full_name=full_name,
            position=position,
            company=company,
            email=email,
            phone=phone,
            message=message,
            marketing_consent=marketing_consent
        )
        messages.success(request, "Ticket booked successfully!")
        return redirect('contact')

    return render(request, "core/contact.html")


def thankyou_views(request):
    return render(request, "core/thankyou.html")






def tnc(request):
    return render(request, 'tnc.html')

def privacy_policy(request):
    return render(request, 'privacy.html')

def refund_policy(request):
    return render(request, 'refund.html')




