from django.shortcuts import render, redirect, get_object_or_404

from .models import Portfolio


# Create your views here.

def portfolio_view(request):
    portfolio = Portfolio.objects.all()
    # portfolio=get_object_or_404(Portfolio)
    context = {
        '  portfolios': portfolio,

    }

    return render(request, 'portfolio/porftolio.html', context)

    # def test_view(request):
    portfolio = Portfolio.objects.all()

    context = {
        '  portfolios': portfolio,

    }
    return render(request, 'portfolio/test.html')
