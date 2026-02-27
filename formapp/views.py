from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

from .forms import ContactForm


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            html = render_to_string(
                'contact/emails/contactform.html',
                {
                    'name': form.cleaned_data['name'],
                    'email': form.cleaned_data['email'],
                },
            )

            send_mail(
                subject='New contact form submission',
                from_email=form.cleaned_data['email'],
                message=(
                    f"Email: {form.cleaned_data['email']}, "
                    f"Name: {form.cleaned_data['name']}"
                ),
                recipient_list=['bm3141838@gmail.com'],
                html_message=html,
            )

            messages.success(request, 'Contact form submitted')
            return redirect('index')
    else:
        form = ContactForm()

    return render(request, 'contact/index.html', {'form': form})
