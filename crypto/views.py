from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import TemplateView

from paystack.signals import payment_verified, successful_payment_signal
from django.dispatch import receiver

from crypto.forms import ContactForm, BuyOrderForm, SellOrderForm
from administrator.models import BitCoinBuyPrice, RippleBuyPrice, EthereumBuyPrice, PerfectMoneyBuyPrice
from administrator.models import BitCoinSellPrice, RippleSellPrice, EthereumSellPrice, PerfectMoneySellPrice
from registered_user.models import BuyOrders, SellOrders
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

    import requests
    import json
    try:
        # crypto Prices
        crypto_price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,LTC,BCH,XRP,EOS,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD")
        crypto_prices = json.loads(crypto_price_request.content)
    except:
        crypto_prices = 'Please check your Internet Connection'
        pass


        # restaurant = User.objects.get(id=restaurant_id)
        #
        # if request.method == "POST":
        #     form = RestaurantSupportTicketForm(request.POST)
        #     if form.is_valid():
        #         check_form = form.save(commit=False)
        #         check_form.user = restaurant
        #         check_form.save()
        #         messages.success(request, "Support Ticket Created")
        #         return redirect('restaurant:support_ticket', restaurant_id)

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = BuyOrderForm(request.POST)
            if form.is_valid():
                check_form = form.save(commit=False)
                check_form.buy_user = request.user
                for item in request.POST:
                    key = item
                    val = request.POST[key]
                    if key == 'csrfmiddlewaretoken':
                        continue
                    else:
                        request.session[key] = val
                # print(request.user, " the user")
                check_form.save()
                request.session['payment_session_id'] = check_form.pk
                return redirect('crypto:make_payment')
            else:
                form = SellOrderForm(request.POST)
                if form.is_valid():
                    check_form = form.save(commit=False)
                    check_form.sell_user = request.user
                    check_form.save()
                    messages.success(request, "Congratulations! We have received your order and we will get back to you. Feel free to contact our support team")
                    return redirect('crypto:landingPage')
                else:
                    messages.success(request, "Something went wrong.... Try again! Make sure the fields are not empty")
                    return redirect('crypto:landingPage')
        else:
            # request.session['']
            return redirect('login')
            # return HttpResponse("PLease Login to continue")
        
    else:
        form = BuyOrderForm()
        args = {
            'btc_price': btc_price, 'ripple_price': ripple_price,
            'ethereum_price': ethereum_price, 'perfect_money_price': perfect_money_price,

            'btc_sell_price': btc_sell_price, 'xrp_sell_price': xrp_sell_price,
            'eth_sell_price': eth_sell_price, 'pm_sell_price': pm_sell_price,

            'form': form, "crypto_prices": crypto_prices
        }
        return render(request, 'crypto/index.html', args)


class Unverified(TemplateView):
    template_name = 'crypto/verification_process.html'


def form_success(request):
    if request.method == 'POST':
        return render(request, 'crypto/form_success.html')
    else:
        return render(request, 'crypto/no_form_submit.html')


def blog(request):
    import requests
    import json
    try:
        # crypto Prices
        crypto_api_price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,LTC,BCH,XRP,EOS,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD,NGN")
        crypto_prices = json.loads(crypto_api_price_request.content)

        # crypto News
        crypto_api_news_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
        crypto_news = json.loads(crypto_api_news_request.content)
        context = {"crypto_news": crypto_news, "crypto_prices": crypto_prices}
    except:
        context = {}
        pass

    return render(request, 'crypto/blog.html', context)

@login_required
def make_payment(request):
    try:
        total = float(request.session['buy_amount_in_ngn'])
        context = {'total': total}
        return render(request, 'crypto/make_payment.html', context)
    except:
        return redirect('crypto:landingPage')


@receiver(successful_payment_signal)
def confirmed_payment(request):
    try:
        payment_session = request.session['payment_session_id']
        print("get the session")
        try:
            buy_order = BuyOrders.objects.filter(id=payment_session).update(paid=True)
            if buy_order:
                del request.session['payment_session_id']
                request.session['success_message'] = True
            print("update d paid button")
        except:
            return redirect('crypto:landingPage')
    except:
        payment_session = None
        pass
    #     # return HttpResponseRedirect(reverse("client:cart_view"))

    return redirect('crypto:landingPage')


# This is paystack receiver
@receiver(payment_verified)
def on_payment_verified(sender, ref, amount, **kwargs):
    """
    ref: paystack reference sent back.
    amount: amount in Naira.
    """
    print('Hey ', str(sender), ' you have successfully paid ', str(amount), '! Here is your reference id ', str(ref))


"Cheks: 08105222561"
