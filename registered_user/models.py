from django.db import models
from login.models import User
from django.urls import reverse

from login.validators import validate_file_size

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)


class CompleteUserRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=GENDER)
    KYC = models.FileField(validators=[validate_file_size])

    def get_absolute_url(self):
        return reverse('registered_user:dashboard')

    # def __str__(self):
    #     return self.first_name + " " + self.last_name


class BitCoin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    NGN = models.FloatField()
    USD = models.FloatField()
    volume = models.FloatField()

    def get_absolute_url(self):
        return reverse('registered_user:dashboard')

    def __str__(self):
        return "BTC " + str(self.volume)


class Ripple(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    NGN = models.FloatField()
    USD = models.FloatField()
    volume = models.FloatField()

    def get_absolute_url(self):
        return reverse('registered_user:dashboard')

    def __str__(self):
        return "XRP " + str(self.volume)


class Ethereum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    NGN = models.FloatField()
    USD = models.FloatField()
    volume = models.FloatField()

    def get_absolute_url(self):
        return reverse('registered_user:dashboard')

    def __str__(self):
        return "E " + str(self.volume)


class PerfectMoney(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    NGN = models.FloatField()
    USD = models.FloatField()
    volume = models.FloatField()

    def get_absolute_url(self):
        return reverse('registered_user:dashboard')

    def __str__(self):
        return "PM " + str(self.volume)

# end of the buy models
# start of the sell models


class SellBitCoin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    NGN = models.FloatField()
    USD = models.FloatField()
    volume = models.FloatField()

    def get_absolute_url(self):
        return reverse('registered_user:dashboard')

    def __str__(self):
        return "BTC " + str(self.volume)


class SellRipple(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    NGN = models.FloatField()
    USD = models.FloatField()
    volume = models.FloatField()

    def get_absolute_url(self):
        return reverse('registered_user:dashboard')

    def __str__(self):
        return "XRP " + str(self.volume)


class SellEthereum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    NGN = models.FloatField()
    USD = models.FloatField()
    volume = models.FloatField()

    def get_absolute_url(self):
        return reverse('registered_user:dashboard')

    def __str__(self):
        return "E " + str(self.volume)


class SellPerfectMoney(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    NGN = models.FloatField()
    USD = models.FloatField()
    volume = models.FloatField()

    def get_absolute_url(self):
        return reverse('registered_user:dashboard')

    def __str__(self):
        return "PM " + str(self.volume)


class BuyOrders(models.Model):
    buy_user = models.ForeignKey(User, on_delete=models.CASCADE)
    buy_coin = models.CharField(max_length=100)
    buy_amount = models.FloatField(max_length=100)
    buy_amount_currency = models.CharField(max_length=20)
    buy_amount_in_ngn = models.FloatField()
    paid = models.BooleanField(default=False)
    order_id = models.CharField(max_length=20, default="ABCD")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return str(self.buy_user) + " - " + self.buy_amount_currency + " " + str(self.buy_amount) + " for " + self.buy_coin  


class SellOrders(models.Model):
    sell_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    sell_coin = models.CharField(max_length=100)
    sell_amount = models.FloatField(max_length=100)
    sell_amount_currency = models.CharField(max_length=20)
    sell_amount_in_ngn = models.FloatField()
    sell_order_id = models.CharField(max_length=20, default="ABCDef")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return str(self.sell_user) + " - " + self.sell_amount_currency + " " + str(self.sell_amount) + " for " + self.sell_coin

