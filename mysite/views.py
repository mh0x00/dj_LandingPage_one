from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'mysite/index.html')
def portfolio_details_view(request):
    return render(request,'mysite/portfolio-details.html')
