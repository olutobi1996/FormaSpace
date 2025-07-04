from django.shortcuts import render

def about(request):
    return render(request, 'branding/about.html', {'video': True})


