from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render(request, 'mysite/index.html')


def error_view(request):
    return render(request, 'mysite/404.html')


def portfolio_details_view(request):
    return render(request, 'mysite/portfolio-details.html')


def service_details_view(request):
    return render(request, 'mysite/service-details.html')


def starter_details_view(request):
    return render(request, 'mysite/starter-page.html')
