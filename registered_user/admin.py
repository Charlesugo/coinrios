from django.contrib import admin
from login.models import User
from registered_user.models import BitCoin, BuyOrders, SellOrders

admin.site.register(BitCoin)
admin.site.register(User)
admin.site.register(BuyOrders)
admin.site.register(SellOrders)
