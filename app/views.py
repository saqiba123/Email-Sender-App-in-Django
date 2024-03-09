from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings



# Create your views here.
def email_sent_success(request):
    return render(request, 'app/success.html')


def email_sender(request):
    if request.method == "POST":
        recipient = request.POST.get('recipient', '')
        subject = request.POST.get('subject','')
        message = request.POST.get('message','')

        send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient] )
         # Redirect to a success page
        return HttpResponseRedirect(reverse('email_sent_success'))

    return render(request, "app/index.html", {"title":"Email Sender App"})
