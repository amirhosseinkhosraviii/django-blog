from django.shortcuts import render, redirect


# Create your views here.


def resume_view(request):
    return render(request, 'resume/resume.html')



