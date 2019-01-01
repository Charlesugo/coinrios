from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from login.models import User
from login.forms import RegisteredUserSignUpForm


class RegisteredUserSignUpView(CreateView):
    model = User
    form_class = RegisteredUserSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Registered User'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('registered_user:dashboard')

"2216133060"

