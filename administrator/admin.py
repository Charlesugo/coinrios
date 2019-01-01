from django.contrib import admin
from administrator.models import BitCoinBuyPrice, BitCoinSellPrice, RippleSellPrice, EthereumSellPrice, PerfectMoneySellPrice
from registered_user.models import CompleteUserRegistration

admin.site.register(BitCoinBuyPrice)
admin.site.register(CompleteUserRegistration)
admin.site.register(BitCoinSellPrice)
admin.site.register(RippleSellPrice)
admin.site.register(EthereumSellPrice)
admin.site.register(PerfectMoneySellPrice)
# admin.site.register(Ethereum)
# admin.site.register(PerfectMoney)
