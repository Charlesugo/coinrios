from django import forms
from crypto.models import Contact
from registered_user.models import BuyOrders, SellOrders


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('email', 'full_name', 'message')


class BuyOrderForm(forms.ModelForm):

    class Meta:
        model = BuyOrders
        fields = ('buy_coin', 'buy_amount', 'buy_amount_currency', 'buy_amount_in_ngn')


class SellOrderForm(forms.ModelForm):

    class Meta:
        model = SellOrders
        fields = ('sell_coin', 'sell_amount', 'sell_amount_currency', 'sell_amount_in_ngn')

