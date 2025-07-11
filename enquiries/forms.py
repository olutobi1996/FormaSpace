from django import forms
from .models import Enquiry
from django import forms
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
        fields = ['name', 'email', 'phone', 'preferred_location', 'space_requirements', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Optional phone number'}),
            'preferred_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Austin, TX'}),
            'space_requirements': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'What kind of space are you looking for?'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Additional message...'}),
        }

from .forms import CustomUserCreationForm  # import your custom form

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

