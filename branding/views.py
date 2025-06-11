from django.shortcuts import render
from .models import BrandNameProposal

def proposals_list(request):
    proposals = BrandNameProposal.objects.all()
    return render(request, 'branding/proposals_list.html', {'proposals': proposals})

