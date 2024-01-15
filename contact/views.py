from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.template.loader import render_to_string
# Create your views here.

def index(request):
    if request.method == 'POST':
        # form = ContactForm(request.POST)
        # name = request.POST['name']
        email = request.POST['email']
        
        # if form.is_valid():
        #     email = form.cleaned_data['email']
            # subscriber = form.save()

            # Send welcome email
        subject = 'Welcome to our Newsletter'
        message = 'Thank you for subscribing to our newsletter!'
        from_email = 'prosperbiz720@gmail.com'
        to_email = [email]
        send_mail(subject, message, from_email, to_email, fail_silently=False)

        return redirect('index') 
        
    return render(request, 'contact/index.html')