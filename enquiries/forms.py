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
        fields = [
            'name',
            'company_name',
            'email',
            'phone',
            'team_size',
            'move_in_timeline',
            'budget_range',
            'space_requirements',
            'message',
            'hear_about_us',
        ]

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Full Name', 'required': True}),
            'company_name': forms.TextInput(attrs={'placeholder': 'Company Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address', 'required': True}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'team_size': forms.TextInput(attrs={'placeholder': 'Number of People / Team Size'}),
            'move_in_timeline': forms.Select(choices=Enquiry._meta.get_field("move_in_timeline").choices),
            'budget_range': forms.TextInput(attrs={'placeholder': 'Budget Range'}),
            'space_requirements': forms.Textarea(attrs={'placeholder': 'Space Requirements', 'rows': 3}),
            'message': forms.Textarea(attrs={'placeholder': 'Additional Details', 'rows': 4}),
            'hear_about_us': forms.TextInput(attrs={'placeholder': 'How did you hear about us?'}),
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

