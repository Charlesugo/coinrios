from django.db import models
from login.models import User
from django.urls import reverse

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
    KYC = models.FileField()

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
