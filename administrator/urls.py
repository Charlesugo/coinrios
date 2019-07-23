from django.urls import path
from administrator import views

app_name = 'administrator'
urlpatterns = [
    path('', views.admin_dashboard, name='adminDashboard'),
    path('delete-form/<pk>/', views.DeleteContactForm.as_view(), name='deleteContactForm'),
    path('delete-buy-order/<pk>/', views.DeleteBuyOrders.as_view(), name='delete_buy_order'),
    path('delete-sell-order/<pk>/', views.DeleteSellOrders.as_view(), name='delete_sell_order'),

    path('bitcoin-exchange-rates/', views.BitCoinExchange.as_view(), name='bitcoinExchangeRates'),
    path('ripple-exchange-rates/', views.RippleExchangeRates.as_view(), name='ripple_exchange_rates'),
    path('ethereum-exchange-rates/', views.EthereumExchangeRates.as_view(), name='ethereum_exchange_rates'),
    path('pm-exchange-rates/', views.PerfectMoneyExchangeRates.as_view(), name='perfect_money_exchange_rates'),

    path('update-bitcoin-price/<pk>/', views.UpdateBitCoinPrice.as_view(), name='update_bit_coin_price'),
    path('update-ripple-price/<pk>/', views.UpdateRippleBuyPrice.as_view(), name='update_ripple_price'),
    path('update-ethereum-price/<pk>/', views.UpdateEthereumBuyPrice.as_view(), name='update_ethereum_price'),
    path('update-pm-price/<pk>/', views.UpdatePerfectMoneyBuyPrice.as_view(), name='update_perfect_money_price'),

    path('bitcoin-buy-requests/', views.BitCoinBuyRequests.as_view(), name='bitcoin_buy_requests'),
    path('ripple-buy-requests/', views.RippleBuyRequests.as_view(), name='ripple_buy_requests'),
    path('ethereum-buy-requests/', views.EthereumBuyRequests.as_view(), name='ethereum_buy_requests'),
    path('perfect-money-buy-requests/', views.PerfectMoneyBuyRequests.as_view(), name='perfect_money_buy_requests'),

    path('bitcoin-sell-requests/', views.BitCoinSellRequests.as_view(), name='bitCoin_sell_request'),
    path('ripple-sell-requests/', views.RippleSellRequests.as_view(), name='ripple_sell_request'),
    path('ethereum-sell-requests/', views.EthereumSellRequests.as_view(), name='ethereum_sell_request'),
    path('pm-sell-requests/', views.PerfectMoneySellRequests.as_view(), name='pm_sell_request'),

    path('update-bitcoin-sell-price/<pk>/', views.UpdateBitCoinSellPrice.as_view(), name='update_bit_coin_sell_price'),
    path('update-ripple-sell-price/<pk>/', views.UpdateRippleSellPrice.as_view(), name='update_ripple_sell_price'),
    path('update-ethereum-sell-price/<pk>/', views.UpdateEthereumSellPrice.as_view(), name='update_ethereum_sell_price'),
    path('update-pm-sell-price/<pk>/', views.UpdatePerfectMoneySellPrice.as_view(), name='update_pm_sell_price'),

    path('users/', views.RegisteredUsers.as_view(), name='registered_users'),
    path('verify-user/<pk>/', views.VerifyRegisteredUser.as_view(), name='verify_registered_user'),
    path('user-profile/<pk>/', views.RegisteredUserProfile.as_view(), name='registered_user_profile'),

    # for the deleting of wrongly created prices
    # path('list-of-eth-prices/', views.ListOfEthereumSellPrices.as_view(), name='list_of_eth_prices'),
    # path('delete-eth/<pk>/', views.DeleteEthereum.as_view(), name='delete_eth'),

]
