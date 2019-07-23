from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from login.models import User
from crypto.models import Contact
from administrator.models import BitCoinBuyPrice, RippleBuyPrice, EthereumBuyPrice, PerfectMoneyBuyPrice
from administrator.models import BitCoinSellPrice, RippleSellPrice, EthereumSellPrice, PerfectMoneySellPrice
from registered_user.models import BitCoin, Ripple, Ethereum, PerfectMoney, BuyOrders, SellOrders
from registered_user.models import SellBitCoin, SellRipple, SellEthereum, SellPerfectMoney
from login.decorators import administrator_required


@login_required
@administrator_required
def admin_dashboard(request):
    buy_orders = BuyOrders.objects.all()
    sell_orders = SellOrders.objects.all()
    contact_form = Contact.objects.all()

    context = {'buy_orders': buy_orders, 'sell_orders': sell_orders, 'contact_form': contact_form}
    template = 'administrator/adminDashboard.html'
    return render(request, template, context)


# for bitcoin rates
@method_decorator([login_required(), administrator_required()], name='dispatch')
class BitCoinExchange(ListView):
    model = BitCoinBuyPrice
    template_name = 'administrator/bitCoinExchange.html'


@method_decorator([login_required(), administrator_required()], name='dispatch')
class UpdateBitCoinPrice(UpdateView):
    model = BitCoinBuyPrice
    fields = ['new_price']
    template_name = 'administrator/updateBitCoinPrice.html'

    def get_context_data(self, **kwargs):
        kwargs['buy_or_sell'] = "BUY"
        return super().get_context_data(**kwargs)
# end of bitcoin rates


# for ripple rates
@method_decorator([login_required(), administrator_required()], name='dispatch')
class RippleExchangeRates(ListView):
    model = RippleBuyPrice
    template_name = 'administrator/rippleExchangeRates.html'


@method_decorator([login_required(), administrator_required()], name='dispatch')
class UpdateRippleBuyPrice(UpdateView):
    model = RippleBuyPrice
    fields = '__all__'
    template_name = 'administrator/updateRippleBuyPrice.html'

    def get_context_data(self, **kwargs):
        kwargs['buy_or_sell'] = "BUY"
        return super().get_context_data(**kwargs)
# end of ripple rates


# for ethereum rates
@method_decorator([login_required(), administrator_required()], name='dispatch')
class EthereumExchangeRates(ListView):
    model = EthereumBuyPrice
    template_name = 'administrator/ethereumExchangeRates.html'


@method_decorator([login_required(), administrator_required()], name='dispatch')
class UpdateEthereumBuyPrice(UpdateView):
    model = EthereumBuyPrice
    fields = '__all__'
    template_name = 'administrator/updateEthereumBuyPrice.html'
# end of ethereum rates


# for perfect money rates
@method_decorator([login_required(), administrator_required()], name='dispatch')
class PerfectMoneyExchangeRates(ListView):
    model = PerfectMoneyBuyPrice
    template_name = 'administrator/perfectMoneyExchangeRates.html'


@method_decorator([login_required(), administrator_required()], name='dispatch')
class UpdatePerfectMoneyBuyPrice(UpdateView):
    model = PerfectMoneyBuyPrice
    fields = '__all__'
    template_name = 'administrator/updatePMBuyPrice.html'
# end of perfect money rates


@method_decorator([login_required(), administrator_required()], name='dispatch')
class BitCoinBuyRequests(ListView):
    model = BitCoin
    context_object_name = 'bit_coin_request'
    template_name = 'administrator/bitCoinBuyRequests.html'


@method_decorator([login_required(), administrator_required()], name='dispatch')
class RippleBuyRequests(ListView):
    model = Ripple
    context_object_name = 'ripple_request'
    template_name = 'administrator/rippleBuyRequests.html'


@method_decorator([login_required(), administrator_required()], name='dispatch')
class EthereumBuyRequests(ListView):
    model = Ethereum
    context_object_name = 'ethereum_request'
    template_name = 'administrator/ethereumBuyRequests.html'


@method_decorator([login_required(), administrator_required()], name='dispatch')
class PerfectMoneyBuyRequests(ListView):
    model = PerfectMoney
    context_object_name = 'perfect_money_request'
    template_name = 'administrator/perfectMoneyBuyRequests.html'


# for the sell requests
@method_decorator([login_required(), administrator_required()], name='dispatch')
class BitCoinSellRequests(ListView):
    model = SellBitCoin
    template_name = 'administrator/bitCoinSellRequests.html'


@method_decorator([login_required(), administrator_required()], name='dispatch')
class RippleSellRequests(ListView):
    model = SellRipple
    template_name = 'administrator/rippleSellRequests.html'


@method_decorator([login_required(), administrator_required()], name='dispatch')
class EthereumSellRequests(ListView):
    model = SellEthereum
    template_name = 'administrator/ethereumSellRequests.html'


@method_decorator([login_required(), administrator_required()], name='dispatch')
class PerfectMoneySellRequests(ListView):
    model = SellPerfectMoney
    template_name = 'administrator/pmSellRequests.html'


@method_decorator([login_required(), administrator_required()], name='dispatch')
class UpdateBitCoinSellPrice(UpdateView):
    model = BitCoinSellPrice
    fields = ['new_price']
    template_name = 'administrator/updateBitCoinPrice.html'

    def get_context_data(self, **kwargs):
        kwargs['buy_or_sell'] = "SELL"
        return super().get_context_data(**kwargs)


@method_decorator([login_required(), administrator_required()], name='dispatch')
class UpdateRippleSellPrice(UpdateView):
    model = RippleSellPrice
    fields = ['new_price']
    template_name = 'administrator/updateRippleBuyPrice.html'

    def get_context_data(self, **kwargs):
        kwargs['buy_or_sell'] = "SELL"
        return super().get_context_data(**kwargs)


@method_decorator([login_required(), administrator_required()], name='dispatch')
class UpdateEthereumSellPrice(UpdateView):
    model = EthereumSellPrice
    fields = ['new_price']
    template_name = 'administrator/updateEthereumBuyPrice.html'

    def get_context_data(self, **kwargs):
        kwargs['buy_or_sell'] = "SELL"
        return super().get_context_data(**kwargs)


@method_decorator([login_required(), administrator_required()], name='dispatch')
class UpdatePerfectMoneySellPrice(UpdateView):
    model = PerfectMoneySellPrice
    fields = ['new_price']
    template_name = 'administrator/updatePMBuyPrice.html'

    def get_context_data(self, **kwargs):
        kwargs['buy_or_sell'] = "SELL"
        return super().get_context_data(**kwargs)


@method_decorator([login_required(), administrator_required()], name='dispatch')
class RegisteredUsers(ListView):
    model = User
    template_name = 'administrator/listOfUsers.html'


@method_decorator([login_required(), administrator_required()], name='dispatch')
class VerifyRegisteredUser(UpdateView):
    model = User
    fields = ['is_verified']
    template_name = 'administrator/verify.html'
    success_url = reverse_lazy('administrator:registered_users')


@method_decorator([login_required(), administrator_required()], name='dispatch')
class RegisteredUserProfile(DetailView):
    model = User
    template_name = 'administrator/profileOfUser.html'


@method_decorator([login_required(), administrator_required()], name='dispatch')
class ListOfContactForms(ListView):
    model = Contact
    template_name = 'administrator/adminDashboard.html'


@method_decorator([login_required(), administrator_required()], name='dispatch')
class DeleteContactForm(DeleteView):
    model = Contact
    success_url = reverse_lazy('administrator:adminDashboard')


@method_decorator([login_required(), administrator_required()], name='dispatch')
class DeleteBuyOrders(DeleteView):
    model = BuyOrders
    success_url = reverse_lazy('administrator:adminDashboard')


class DeleteSellOrders(DeleteView):
    model = SellOrders
    success_url = reverse_lazy('administrator:adminDashboard')

# for the deleting of wrongly created prices
# class ListOfEthereumSellPrices(ListView):
#     model = EthereumSellPrice
#     template_name = 'administrator/ethSellPrice.html'


# class DeleteEthereum(DeleteView):
#     model = EthereumSellPrice
#     success_url = reverse_lazy('administrator:adminDashboard')

