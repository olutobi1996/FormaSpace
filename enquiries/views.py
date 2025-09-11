from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect 
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.conf import settings
from .forms import EnquiryForm, SubscriberForm, CustomUserCreationForm
from urllib.parse import urlencode
from django.contrib import messages  
from .forms import EnquiryForm
from .models import Enquiry, Subscriber


def enquiry_create(request): 
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            enquiry = form.save()

            # ✅ Send notification to Gmail
            send_mail(
                subject=f'New Enquiry from {enquiry.name}',
                message=(
                    f"Name: {enquiry.name}\n"
                    f"Company: {enquiry.company_name}\n"
                    f"Email: {enquiry.email}\n"
                    f"Phone: {enquiry.phone}\n"
                    f"Team Size: {enquiry.team_size}\n"
                    f"Move-in Timeline: {enquiry.move_in_timeline}\n"
                    f"Budget Range: {enquiry.budget_range}\n"
                    f"Requirements: {enquiry.space_requirements}\n"
                    f"Hear About Us: {enquiry.hear_about_us}\n\n"
                    f"Message:\n{enquiry.message}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,  # enquiries@formaspace.co.uk
                recipient_list=["formaspaceoffice@gmail.com"],  # your Gmail inbox
                fail_silently=False,
            )

            # ✅ Confirmation email to user
            send_mail(
                subject="Thanks for your enquiry — FormaSpace",
                message=(
                    f"Hi {enquiry.name},\n\n"
                    "Thanks for reaching out to FormaSpace! "
                    "We've received your enquiry and will get back to you shortly.\n\n"
                    "— The FormaSpace Team"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[enquiry.email],
                fail_silently=False,
            )

            return redirect('enquiries:thank_you')
    else:
        form = EnquiryForm()

    return render(request, 'registration/enquiry_form.html', {'form': form})


def thank_you(request):
    return render(request, 'registration/thank_you.html')


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
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
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=False,
            )

            return redirect('registration:thank_you')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})


def subscribe_newsletter(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if email:
            subscriber, created = Subscriber.objects.get_or_create(email=email)
            try:
                send_mail(
                    subject="Welcome to FormaSpace News!",
                    message=(
                        f"Hi there,\n\nThanks for subscribing to FormaSpace News. "
                        "We'll keep you updated with the latest insights and updates!\n\n"
                        "— The FormaSpace Team"
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[email],
                    fail_silently=False,
                )
                messages.success(request, "✅ Thanks for subscribing! Please check your email.")
            except Exception as e:
                messages.error(request, f"⚠️ Subscription saved, but email failed: {str(e)}")

        else:
            messages.error(request, "⚠️ Please enter a valid email.")

        return redirect(request.META.get("HTTP_REFERER", "/"))

    return redirect("enquiries:enquiry_create")








