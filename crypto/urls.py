from django.urls import path
from crypto import views

app_name = 'crypto'
urlpatterns = [
    path('', views.index, name='landingPage'),
    path('blog/', views.blog, name='blog'),
    path('unverified/', views.Unverified.as_view(), name='verification_process'),
    path('form-success/', views.form_success, name='form_success'),

    path('make_payment/', views.make_payment, name='make_payment'),
    path('confirmed-payment/', views.confirmed_payment, name='confirmed_payment'),
]
