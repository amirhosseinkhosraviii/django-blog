from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Contact
from .forms import ContactForm
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def contact_view(request):
    if request.method == "Post":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    contact = Contact.objects.all()
    context = {}
    return render(request, 'contact/contact.html', {'form': form})
