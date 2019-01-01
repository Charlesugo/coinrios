from django import forms
from registered_user.models import BitCoin, Ripple, Ethereum, PerfectMoney, CompleteUserRegistration
from registered_user.models import SellBitCoin, SellRipple, SellEthereum, SellPerfectMoney


class BitCoinForm(forms.ModelForm):

    class Meta:
        model = BitCoin
        fields = ('NGN', 'USD', 'volume')


class RippleForm(forms.ModelForm):

    class Meta:
        model = Ripple
        fields = ('NGN', 'USD', 'volume')


class EthereumForm(forms.ModelForm):

    class Meta:
        model = Ethereum
        fields = ('NGN', 'USD', 'volume')


class PerfectMoneyForm(forms.ModelForm):

    class Meta:
        model = PerfectMoney
        fields = ('NGN', 'USD', 'volume')

# end of sell forms
# for registration


class CompleteUserRegistrationForm(forms.ModelForm):

    class Meta:
        model = CompleteUserRegistration
        fields = ('first_name', 'last_name', 'email', 'gender', 'KYC')

# start of sell forms


class SellBitCoinForm(forms.ModelForm):

    class Meta:
        model = SellBitCoin
        fields = ('NGN', 'USD', 'volume')


class SellRippleForm(forms.ModelForm):

    class Meta:
        model = SellRipple
        fields = ('NGN', 'USD', 'volume')


class SellEthereumForm(forms.ModelForm):

    class Meta:
        model = SellEthereum
        fields = ('NGN', 'USD', 'volume')


class SellPerfectMoneyForm(forms.ModelForm):

    class Meta:
        model = SellPerfectMoney
        fields = ('NGN', 'USD', 'volume')

