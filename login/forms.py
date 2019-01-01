from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms
from login.models import User


class AdministratorSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_administrator = True
        user.save()
        # administrator = RegisteredAdministrator.objects.create(user=user)


class RegisteredUserSignUpForm(UserCreationForm):
    email = forms.EmailField()
    address = forms.CharField(max_length=200)
    city = forms.CharField(max_length=200)
    state = forms.CharField(max_length=200)
    country = forms.CharField(max_length=200)
    drivers_license_or_international_passport_or_national_id_card = forms.FileField()
    utility_bill = forms.FileField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'address', 'city', 'state', 'country',
            'drivers_license_or_international_passport_or_national_id_card', 'utility_bill', 'password1', 'password2'
        )

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_registered_user = True
        user.save()
        # teacher = RegisteredTeacher.objects.create(user=user)


class VerifyRegisteredUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'username', 'is_verified',
        )

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_verified = True
        user.save()

