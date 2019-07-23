from django.urls import path
from registered_user import views

app_name = 'registered_user'
urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    path('sell/', views.Sell.as_view(), name='sell'),
    path('orders/', views.orders, name='orders'),
    # path('', views.dashboard, name='dashboard'),

    path('bitcoin-buy-price/', views.BitCoinBuyView.as_view(), name='bitcoin_buy_price'),

    path('profile/[{`<pk>^#}]/', views.UserProfile.as_view(), name='user_profile'),
    # path('bitcoin-profile/<pk>/', views.BitcoinUserProfile.as_view(), name='bitcoin_user_profile'),

    path('bitcoin/[{`<bitcoin_id>^#}]/', views.bitcoin_view, name='bitcoin'),
    path('ripple/[{`<ripple_id>^#}]/', views.ripple_view, name='ripple'),
    path('ethereum/[{`<ethereum_id>^#}]/', views.ethereum_view, name='ethereum'),
    path('perfect-money/[{`<perfect_money_id>^#}]/', views.perfect_money_view, name='perfect_money'),

    path('sell-bitcoin/[{`<bitcoin_id>^#}]/', views.sell_bitcoin_view, name='sell_bitcoin'),
    path('sell-ripple/[{`<ripple_id>^#}]/', views.sell_ripple_view, name='sell_ripple'),
    path('sell-ethereum/[{`<ethereum_id>^#}]/', views.sell_ethereum_view, name='sell_ethereum'),
    path('sell-pm/[{`<perfect_money_id>^#}]/', views.sell_perfect_money_view, name='sell_perfect_money'),

]
