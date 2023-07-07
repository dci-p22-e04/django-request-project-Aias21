from django.urls import path
from .views import home, save_currencies

app_name = 'currency_exchange'

urlpatterns = [
    path('', home, name="home"),
    path('save/', save_currencies, name='save_currencies'),
]