from django.shortcuts import render, redirect
from .forms import EnquiryForm

def enquiry_create(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enquiries:thank_you')
    else:
        form = EnquiryForm()
    return render(request, 'enquiries/enquiry_form.html', {'form': form})

def thank_you(request):
    return render(request, 'enquiries/thank_you.html')
