from .forms import EnquiryForm, SubscriberForm


def enquiry_form_context(request):
    return {
        'enquiry_form': EnquiryForm(),
        'subscription_form': SubscriberForm(),  # add subscription form here
    }
