from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Contact
from .forms import ContactForm
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def contact_view(request):
    if request.method == "Post":
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message_subject = request.POST['message_subject']
        return redirect(request, 'contact/contact.html', {'message_name': message_name})



    else:
        form = ContactForm()
    contact = Contact.objects.all()
    context = {}
    return render(request, 'contact/contact.html', {'form': form})
