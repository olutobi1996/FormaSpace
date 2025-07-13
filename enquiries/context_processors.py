from .forms import EnquiryForm

def enquiry_form_context(request):
    return {
        'enquiry_form': EnquiryForm()
    }
