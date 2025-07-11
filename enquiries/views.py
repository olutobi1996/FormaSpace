from django.shortcuts import render, redirect
from .forms import EnquiryForm
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse

@login_required
def enquiry_create(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            enquiry = form.save()

            # Send notification to FormaSpace team
            send_mail(
                subject=f'New Enquiry from {enquiry.name}',
                message=enquiry.message,
                from_email=enquiry.email,
                recipient_list=['you@formaspace.com'],  # Update this email
                fail_silently=False,
            )

            # Send confirmation to user
            send_mail(
                subject="Thanks for your enquiry — FormaSpace",
                message=(
                    f"Hi {enquiry.name},\n\n"
                    "Thanks for reaching out to FormaSpace! "
                    "We've received your message and will get back to you shortly.\n\n"
                    "— The FormaSpace Team"
                ),
                from_email='you@formaspace.com',
                recipient_list=[enquiry.email],
                fail_silently=False,
            )

            return redirect('registration:thank_you')
    else:
        initial_data = {}
        if request.user.is_authenticated:
            initial_data = {
                'name': request.user.get_full_name() or request.user.username,
                'email': request.user.email,
            }
        form = EnquiryForm(initial=initial_data)

    return render(request, 'registration/enquiry_form.html', {'form': form})


def thank_you(request):
    return render(request, 'registration/thank_you.html')


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            # Send welcome email
            send_mail(
                subject="Welcome to FormaSpace!",
                message=(
                    f"Hi {user.username},\n\n"
                    "Thanks for signing up with FormaSpace. "
                    "You can now book rooms and submit enquiries through your account.\n\n"
                    "— The FormaSpace Team"
                ),
                from_email='you@formaspace.com',
                recipient_list=[user.email],
                fail_silently=False,
            )

            # Redirect to thank you page with a URL param for auto-redirect if you want
            return redirect('enquiries:thank_you')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})

