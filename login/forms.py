from django import forms
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.shortcuts import redirect
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
    # address = forms.CharField(max_length=200)
    # city = forms.CharField(max_length=200)
    # state = forms.CharField(max_length=200)
    # country = forms.CharField(max_length=200)
    # drivers_license_or_international_passport_or_national_id_card = forms.FileField()
    # utility_bill = forms.FileField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username', 'email'
        )
        # , 'first_name', 'last_name', 'address', 'city', 'state', 'country',
        #  'drivers_license_or_international_passport_or_national_id_card', 'utility_bill', 'password1', 'password2'

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_registered_user = True
        get_email = self.cleaned_data['email']
        try:
            check_email = User.objects.filter(email=get_email).count()
            if check_email > 0:
                print('error')
                self.request.session['recent'] = True
                raise forms.ValidationError("This email has already been registered. Please use another email")
            else:
                user.save()
        except:
            return redirect('create_registered_user')
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

