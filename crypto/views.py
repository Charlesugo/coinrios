from django.shortcuts import render, redirect
from crypto.forms import ContactForm
from django.views.generic import TemplateView

from administrator.models import BitCoinBuyPrice, RippleBuyPrice, EthereumBuyPrice, PerfectMoneyBuyPrice
from administrator.models import BitCoinSellPrice, RippleSellPrice, EthereumSellPrice, PerfectMoneySellPrice
#   min-api.cryptocompare.com
#   codemy.com
#   coinmarketcap.com


def index(request):
    btc_price = BitCoinBuyPrice.objects.get()
    ripple_price = RippleBuyPrice.objects.get()
    ethereum_price = EthereumBuyPrice.objects.get()
    perfect_money_price = PerfectMoneyBuyPrice.objects.get()

    btc_sell_price = BitCoinSellPrice.objects.get()
    xrp_sell_price = RippleSellPrice.objects.get()
    eth_sell_price = EthereumSellPrice.objects.get()
    pm_sell_price = PerfectMoneySellPrice.objects.get()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crypto:form_success')

    else:
        form = ContactForm()
        args = {
            'btc_price': btc_price, 'ripple_price': ripple_price,
            'ethereum_price': ethereum_price, 'perfect_money_price': perfect_money_price,

            'btc_sell_price': btc_sell_price, 'xrp_sell_price': xrp_sell_price,
            'eth_sell_price': eth_sell_price, 'pm_sell_price': pm_sell_price,

            'form': form
        }
        return render(request, 'crypto/index.html', args)


class Unverified(TemplateView):
    template_name = 'crypto/verification_process.html'


def form_success(request):
    if request.method == 'POST':
        return render(request, 'crypto/form_success.html')
    else:
        return render(request, 'crypto/no_form_submit.html')



"Cheks: 08105222561"
