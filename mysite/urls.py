from django.urls import path
from mysite.views import home_view, portfolio_details_view, service_details_view, starter_details_view, error_view

app_name = 'mysite'

urlpatterns = [
    path('', home_view, name='home'),
    path('portfolio', portfolio_details_view, name='portfolio'),
    path('error', error_view, name='error'),
    path('starter', starter_details_view, name='starter'),
    path('service', service_details_view, name='servise')
]
