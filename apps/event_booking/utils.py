import io
import threading
from django.template.loader import get_template
from django.core.mail import EmailMessage
from xhtml2pdf import pisa

def generate_pdf_ticket(template_src, context_dict):
    """HTML template ko PDF bytes me render karta hai."""
    template = get_template(template_src)
    html = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return result.getvalue()
    return None

def _send_ticket_worker(user_details):
    """Background worker jo PDF generate karke email bhejta hai."""
    context = {
        'user_details': user_details,
        'event': user_details.event_details,
    }

    pdf_bytes = generate_pdf_ticket('event_booking/ticket-pdf-template.html', context)
    
    if pdf_bytes:
        subject = f"Booking Confirmation & Entry Ticket: {user_details.event_details.title}"
        body = (
            f"Hi {user_details.full_name},\n\n"
            f"Your booking for '{user_details.event_details.title}' is confirmed.\n\n"
            f"Event Date: {user_details.event_details.start_date}\n"
            f"Venue: {user_details.event_details.venue}\n"
            f"Tickets: {user_details.quantity}\n\n"
            f"Please find your attached PDF Ticket. You will need to show this at the entrance.\n\n"
            f"Best regards,\n"
            f"{user_details.event_details.organizer or 'Event Management Team'}"
        )

        email = EmailMessage(
            subject=subject,
            body=body,
            from_email=None,
            to=[user_details.email]
        )
        email.attach(f"Ticket_{user_details.uid}.pdf", pdf_bytes, "application/pdf")
        email.send(fail_silently=False)

def send_ticket_email(user_details):
    """Email process ko alag thread me run karta hai taaki browser freeze na ho."""
    threading.Thread(target=_send_ticket_worker, args=(user_details,)).start()