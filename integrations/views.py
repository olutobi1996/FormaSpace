from django.shortcuts import render

def integration_list(request):
    return render(request, 'integrations/integration_list.html')
