from django import forms
from .models import Enquiry
from .models import Subscriber
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['name', 'phone', 'email', 'space_requirements', 'message']  # Removed preferred_location

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Name',
                'required': True,
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Phone',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email Address',
                'required': True,
            }),
            'space_requirements': forms.TextInput(attrs={
                'placeholder': 'Space Requirements',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Message',
                'rows': 4,
                'required': True,
            }),
        }


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            send_mail(
                subject="Welcome to FormaSpace!",
                message=(
                    f"Hi {user.username},\n\n"
                    "Thanks for signing up with FormaSpace. "
                    "You can now book rooms and submit enquiries through your account.\n\n"
                    "— The FormaSpace Team"
                ),
                from_email='you@formaspace.com',
                recipient_list=[user.email],  # this will now exist
                fail_silently=False,
            )

            return redirect('enquiries:thank_you')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})



class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email',
                'class': 'form-control',
            })
        }

