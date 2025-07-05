from django.shortcuts import render

def connectivity_view(request):
    return render(request, 'pages/connectivity.html')  

