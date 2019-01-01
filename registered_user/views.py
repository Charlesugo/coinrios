from django.shortcuts import render, redirect
from login.models import User
from registered_user.forms import BitCoinForm, RippleForm, EthereumForm, PerfectMoneyForm
from registered_user.forms import SellBitCoinForm, SellRippleForm, SellEthereumForm, SellPerfectMoneyForm

from administrator.models import BitCoinBuyPrice, RippleBuyPrice, EthereumBuyPrice, PerfectMoneyBuyPrice
from administrator.models import BitCoinSellPrice, RippleSellPrice, EthereumSellPrice, PerfectMoneySellPrice
from login.decorators import registered_user_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, ListView


@method_decorator([login_required(), registered_user_required()], name='dispatch')
class BitCoinBuyView(ListView):
    model = BitCoinBuyPrice
    template_name = 'registered_user/bitPrice.html'


@method_decorator([login_required(), registered_user_required()], name='dispatch')
class Dashboard(TemplateView):
    template_name = 'registered_user/index.html'

    def get_context_data(self, **kwargs):
        btc_price = BitCoinBuyPrice.objects.get()
        ripple_price = RippleBuyPrice.objects.get()
        ethereum_price = EthereumBuyPrice.objects.get()
        perfect_money_price = PerfectMoneyBuyPrice.objects.get()

        btc_sell_price = BitCoinSellPrice.objects.get()
        xrp_sell_price = RippleSellPrice.objects.get()
        eth_sell_price = EthereumSellPrice.objects.get()
        pm_sell_price = PerfectMoneySellPrice.objects.get()

        kwargs['btc_price'] = str(btc_price)
        kwargs['ripple_price'] = str(ripple_price)
        kwargs['ethereum_price'] = str(ethereum_price)
        kwargs['perfect_money_price'] = str(perfect_money_price)

        kwargs['btc_sell_price'] = str(btc_sell_price)
        kwargs['xrp_sell_price'] = str(xrp_sell_price)
        kwargs['eth_sell_price'] = str(eth_sell_price)
        kwargs['pm_sell_price'] = str(pm_sell_price)
        return super().get_context_data(**kwargs)

    # def get_context_data(self, **kwargs):
        # Get crypto data
        # import requests
        # import json
        # crypto_api_req = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP&syms=USD")
        # crypto_api = json.loads(crypto_api_req.content)

        # kwargs['cryptoCurrencies'] = "crypto_api"
        # return super().get_context_data(**kwargs)


@method_decorator([login_required(), registered_user_required()], name='dispatch')
class Sell(TemplateView):
    template_name = 'registered_user/sell.html'

    def get_context_data(self, **kwargs):
        btc_price = BitCoinBuyPrice.objects.get()
        ripple_price = RippleBuyPrice.objects.get()
        ethereum_price = EthereumBuyPrice.objects.get()
        perfect_money_price = PerfectMoneyBuyPrice.objects.get()

        btc_sell_price = BitCoinSellPrice.objects.get()
        xrp_sell_price = RippleSellPrice.objects.get()
        eth_sell_price = EthereumSellPrice.objects.get()
        pm_sell_price = PerfectMoneySellPrice.objects.get()

        kwargs['btc_price'] = str(btc_price)
        kwargs['ripple_price'] = str(ripple_price)
        kwargs['ethereum_price'] = str(ethereum_price)
        kwargs['perfect_money_price'] = str(perfect_money_price)

        kwargs['btc_sell_price'] = str(btc_sell_price)
        kwargs['xrp_sell_price'] = str(xrp_sell_price)
        kwargs['eth_sell_price'] = str(eth_sell_price)
        kwargs['pm_sell_price'] = str(pm_sell_price)
        return super().get_context_data(**kwargs)


@login_required
@registered_user_required()
def bitcoin_view(request, bitcoin_id):
    import requests
    import json
    user = User.objects.get(id=bitcoin_id)
    # for the price of buy exchange for bit coin
    btc_price = BitCoinBuyPrice.objects.get()
    # crypto_api_req = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=USD,NGN")
    # btc = json.loads(crypto_api_req.content)

    if request.method == "POST":
        form = BitCoinForm(request.POST)
        if form.is_valid():
            check_form = form.save(commit=False)
            check_form.user = user
            check_form.save()
            return redirect('registered_user:dashboard')
            
    else:
        form = BitCoinForm()
        args = {'user': user, 'form': form, 'btc': "btc", 'btc_price': btc_price}
        return render(request, 'registered_user/bitcoin.html', args)


@method_decorator([login_required(), registered_user_required()], name='dispatch')
class UserProfile(DetailView):
    model = User
    template_name = 'registered_user/UserProfile.html'


@method_decorator([login_required(), registered_user_required()], name='dispatch')
class BitcoinUserProfile(DetailView):
    model = User
    template_name = 'registered_user/BitcoinUserProfile.html'


@login_required
@registered_user_required()
def ripple_view(request, ripple_id):
    import requests
    import json
    user = User.objects.get(id=ripple_id)
    # for the price of buy exchange for xrp coin
    ripple_price = RippleBuyPrice.objects.get()
    # crypto_api_req = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=XRP&tsyms=USD,NGN")
    # btc = json.loads(crypto_api_req.content)

    if request.method == "POST":
        form = RippleForm(request.POST)
        if form.is_valid():
            check_form = form.save(commit=False)
            check_form.user = user
            check_form.save()
            return redirect('registered_user:dashboard')

    else:
        form = RippleForm()
        args = {'user': user, 'form': form, 'xrp': "xrp", 'ripple_price': ripple_price}
        return render(request, 'registered_user/ripple.html', args)


@login_required
@registered_user_required()
def ethereum_view(request, ethereum_id):
    import requests
    import json
    user = User.objects.get(id=ethereum_id)
    # for the price of buy exchange for xrp coin
    ethereum_price = EthereumBuyPrice.objects.get()
    # crypto_api_req = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=XRP&tsyms=USD,NGN")
    # btc = json.loads(crypto_api_req.content)

    if request.method == "POST":
        form = EthereumForm(request.POST)
        if form.is_valid():
            check_form = form.save(commit=False)
            check_form.user = user
            check_form.save()
            return redirect('registered_user:dashboard')

    else:
        form = EthereumForm()
        args = {'user': user, 'form': form, 'eth': "eth", 'ethereum_price': ethereum_price}
        return render(request, 'registered_user/ethereum.html', args)


@login_required
@registered_user_required()
def perfect_money_view(request, perfect_money_id):
    import requests
    import json
    user = User.objects.get(id=perfect_money_id)
    # for the price of buy exchange for xrp coin
    perfect_money_price = PerfectMoneyBuyPrice.objects.get()
    # crypto_api_req = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=XRP&tsyms=USD,NGN")
    # btc = json.loads(crypto_api_req.content)

    if request.method == "POST":
        form = PerfectMoneyForm(request.POST)
        if form.is_valid():
            check_form = form.save(commit=False)
            check_form.user = user
            check_form.save()
            return redirect('registered_user:dashboard')

    else:
        form = PerfectMoneyForm()
        args = {'user': user, 'form': form, 'eth': "eth", 'perfect_money_price': perfect_money_price}
        return render(request, 'registered_user/perfect_money.html', args)

# The Buy functions ends

# The sell functions begins


@login_required
@registered_user_required()
def sell_bitcoin_view(request, bitcoin_id):
    import requests
    import json
    user = User.objects.get(id=bitcoin_id)
    # for the price of buy exchange for bit coin
    btc_sell_price = BitCoinSellPrice.objects.get()
    # crypto_api_req = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=USD,NGN")
    # btc = json.loads(crypto_api_req.content)

    if request.method == "POST":
        form = SellBitCoinForm(request.POST)
        if form.is_valid():
            check_form = form.save(commit=False)
            check_form.user = user
            check_form.save()
            return redirect('registered_user:dashboard')

    else:
        form = SellBitCoinForm()
        args = {'user': user, 'form': form, 'btc': "btc", 'btc_sell_price': btc_sell_price}
        return render(request, 'registered_user/sellBitCoin.html', args)


@login_required
@registered_user_required()
def sell_ripple_view(request, ripple_id):
    import requests
    import json
    user = User.objects.get(id=ripple_id)
    # for the price of buy exchange for bit coin
    xrp_sell_price = RippleSellPrice.objects.get()
    # crypto_api_req = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=USD,NGN")
    # btc = json.loads(crypto_api_req.content)

    if request.method == "POST":
        form = SellRippleForm(request.POST)
        if form.is_valid():
            check_form = form.save(commit=False)
            check_form.user = user
            check_form.save()
            return redirect('registered_user:dashboard')

    else:
        form = SellRippleForm()
        args = {'user': user, 'form': form, 'btc': "btc", 'xrp_sell_price': xrp_sell_price}
        return render(request, 'registered_user/sellRipple.html', args)


@login_required
@registered_user_required()
def sell_ethereum_view(request, ethereum_id):
    import requests
    import json
    user = User.objects.get(id=ethereum_id)
    # for the price of buy exchange for bit coin
    eth_sell_price = EthereumSellPrice.objects.get()
    # crypto_api_req = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=USD,NGN")
    # btc = json.loads(crypto_api_req.content)

    if request.method == "POST":
        form = SellEthereumForm(request.POST)
        if form.is_valid():
            check_form = form.save(commit=False)
            check_form.user = user
            check_form.save()
            return redirect('registered_user:dashboard')

    else:
        form = SellEthereumForm()
        args = {'user': user, 'form': form, 'btc': "btc", 'eth_sell_price': eth_sell_price}
        return render(request, 'registered_user/sellEthereum.html', args)


@login_required
@registered_user_required()
def sell_perfect_money_view(request, perfect_money_id):
    import requests
    import json
    user = User.objects.get(id=perfect_money_id)
    # for the price of buy exchange for bit coin
    pm_sell_price = PerfectMoneySellPrice.objects.get()
    # crypto_api_req = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=USD,NGN")
    # btc = json.loads(crypto_api_req.content)

    if request.method == "POST":
        form = SellPerfectMoneyForm(request.POST)
        if form.is_valid():
            check_form = form.save(commit=False)
            check_form.user = user
            check_form.save()
            return redirect('registered_user:dashboard')

    else:
        form = SellPerfectMoneyForm()
        args = {'user': user, 'form': form, 'btc': "btc", 'pm_sell_price': pm_sell_price}
        return render(request, 'registered_user/sellPerfectMoney.html', args)

