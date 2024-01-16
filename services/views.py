from django.shortcuts import render, redirect


# Create your views here.
def services_view(request):
    return render(request, 'services/services.html')
