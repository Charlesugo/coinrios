from django.urls import path
from crypto import views

app_name = 'crypto'
urlpatterns = [
    path('', views.index, name='landingPage'),
    path('unverified/', views.Unverified.as_view(), name='verification_process'),
    path('form-success/', views.form_success, name='form_success'),
]
