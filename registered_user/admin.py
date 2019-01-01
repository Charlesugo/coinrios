from django.contrib import admin
from login.models import User
from registered_user.models import BitCoin

admin.site.register(BitCoin)
admin.site.register(User)
