from django.urls import path
from mysite.views import home_view, portfolio_details_view

app_name = 'mysite'

urlpatterns = [
    path('', home_view, name='home'),
    path('portfolio', portfolio_details_view, name='portfolio')
]
