from django.shortcuts import render

# Create your views here.


def blog_view(request):
    return render(request, 'blogs/blog.html')


def blog_details_view(request):
    return render(request, 'blogs/blog-details.html')
