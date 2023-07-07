from django import forms
from currency_exchange.models import ExchangeRate


class ExchangeForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(ExchangeForm, self).__init__(*args, **kwargs)
        currencies = ExchangeRate.objects.values_list('currency', 'currency')
        placeholder = (None, "--Select a currency--")
        self.fields['from_currency'] = forms.ChoiceField(choices=[placeholder] + list(currencies), initial=None)
        self.fields['to_currency'] = forms.ChoiceField(choices=[placeholder] + list(currencies), initial=None)
    amount = forms.IntegerField()



