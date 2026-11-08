from django.urls import path
from blog.views import blog_view, blog_details_view

app_name = 'blogs'

urlpatterns = [
    path('', blog_view, name='blog'),
    path('blog_details', blog_details_view, name='blog_details')
]
