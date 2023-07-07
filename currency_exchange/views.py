from django.shortcuts import render, redirect
import requests
import datetime
from .forms import ExchangeForm
from .models import ExchangeRate

API_KEY = "Your api key here!"


def home(request):
    if request.method == 'POST':
        form = ExchangeForm(request.POST)
        if form.is_valid():
            base_currency = form.cleaned_data['from_currency']
            conversion_currency = form.cleaned_data['to_currency']
            amount = form.cleaned_data['amount']

            base_rate = get_exchange_rate(base_currency)
            conversion_rate = get_exchange_rate(conversion_currency)

            if base_rate and conversion_rate:
                converted_amount = (amount / base_rate) * conversion_rate
                return render(request, 'home.html', {'form': form, 'converted_amount': round(converted_amount, 2),
                                                     'conversion_rate':conversion_currency})
            else:
                error_message = "Error: Unable to fetch exchange rates."
                return render(request, 'home.html', {'form': form, 'error_message': error_message})

    else:
        form = ExchangeForm()

    return render(request, 'home.html', {'form': form})


def get_exchange_rate(currency):
    try:
        exchange_rate = ExchangeRate.objects.filter(currency=currency).latest('date')
        return exchange_rate.rate
    except ExchangeRate.DoesNotExist:
        return None


def save_currencies(request):
    url = "http://api.exchangeratesapi.io/v1/latest"
    params = {"base": "EUR", "access_key": API_KEY}
    response = requests.get(url=url, params=params)

    if response.status_code == 200:
        data = response.json()
        date = datetime.date.today()

        rates = data.get('rates')

        for currency, rate in rates.items():
            try:
                exchange_rate = ExchangeRate.objects.filter(currency=currency).latest('date')
                exchange_rate.rate = rate
                exchange_rate.date = date
                exchange_rate.save()
            except ExchangeRate.DoesNotExist:
                exchange_rate = ExchangeRate.objects.create(currency=currency, rate=rate, date=date)

        return redirect('currency_exchange:home')
    else:
        data = {}

    return render(request, 'home.html', {'data': data})