from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail,EmailMessage
import smtplib
# Create your views here.

def error_404_view(request, exception):
    return render(request,"404.html")
def home(request):
    try:
        if request.method == "POST":
            message_name = request.POST["name"].strip()
            message_email =  request.POST["email"].strip().lower()
            message_sub =  request.POST["subject"]
            message =  request.POST["message"]

            email_message = f'Message received from Name :{message_name}, Email: {message_email}\n\n{message}'
        
            subject =message_sub
            message = email_message
            from_email = message_name+"<bryteredunuakoh@gmail.com>"  # Sender's email address
            recipient_list = ['bright.wiredu@aims.ac.rw']  # List of recipient email addresses

            send_mail(subject, message, from_email, recipient_list)

            subject_user = f'We received your message {message_name}'
            message_user = 'We received your enquiry! Our team will get back to you as soon as possible.'
            from_email_user = "Bright Nuakoh Wiredu <bryteredunuakoh@gmail.com>"  # Sender's email address
            send_mail(subject_user, message_user,from_email_user, [message_email])
            context = {
                 'success':[f'Your Message has been sent successfully, {message_name}'],

            }

            return  render(request, "index.html",context)
        
        else:
            return  render(request, "index.html")
        
    except smtplib.SMTPRecipientsRefused:
            context ={
                    "errors" : ['Invalid Email!'],
                    }
            return  render(request, "index.html",context)
    
def index(request):
    return render(request, "index.html")

def portfolio(request):
    return render(request, "portfolio-details.html")

def portfolio2(request):
    return render(request, "portfolio-details2.html")

def portfolio3(request):
    return render(request, "portfolio-details3.html")