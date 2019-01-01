from django.db import models
from django.shortcuts import reverse


class BitCoinBuyPrice(models.Model):
    new_price = models.FloatField()

    def get_absolute_url(self):
        return reverse('administrator:adminDashboard')

    def __str__(self):
        return "NGN " + str(self.new_price)


class BitCoinSellPrice(models.Model):
    new_price = models.FloatField()

    def get_absolute_url(self):
        return reverse('administrator:adminDashboard')

    def __str__(self):
        return "NGN " + str(self.new_price)


class RippleBuyPrice(models.Model):
    new_price = models.FloatField()

    def get_absolute_url(self):
        return reverse('administrator:adminDashboard')

    def __str__(self):
        return "NGN " + str(self.new_price)


class RippleSellPrice(models.Model):
    new_price = models.FloatField()

    def get_absolute_url(self):
        return reverse('administrator:adminDashboard')

    def __str__(self):
        return "NGN " + str(self.new_price)


class EthereumBuyPrice(models.Model):
    new_price = models.FloatField()

    def get_absolute_url(self):
        return reverse('administrator:adminDashboard')

    def __str__(self):
        return "NGN " + str(self.new_price)


class EthereumSellPrice(models.Model):
    new_price = models.FloatField()

    def get_absolute_url(self):
        return reverse('administrator:adminDashboard')

    def __str__(self):
        return "NGN " + str(self.new_price)


class PerfectMoneyBuyPrice(models.Model):
    new_price = models.FloatField()

    def get_absolute_url(self):
        return reverse('administrator:adminDashboard')

    def __str__(self):
        return "NGN " + str(self.new_price)


class PerfectMoneySellPrice(models.Model):
    new_price = models.FloatField()

    def get_absolute_url(self):
        return reverse('administrator:adminDashboard')

    def __str__(self):
        return "NGN " + str(self.new_price)
