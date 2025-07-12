from django.shortcuts import render
from core.models import MyVideo
from enquiries.forms import SubscriberForm


def home(request):
    video = MyVideo.objects.first()
    subscription_form = SubscriberForm()

    subscribed = request.GET.get('subscribed')
    subscription_success = None
    subscription_error = None

    if subscribed == '1':
        subscription_success = "You are now part of the FormaSpace family!"
    elif subscribed == '0':
        subscription_error = "There was an error with your subscription. Please try again."

    return render(request, 'core/home.html', {
        'video': video,
        'subscription_form': subscription_form,
        'subscription_success': subscription_success,
        'subscription_error': subscription_error,
    })


