from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from login.models import User
from login.forms import AdministratorSignUpForm


class AdministratorSignUpView(CreateView):
    model = User
    form_class = AdministratorSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Administrator'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('administrator:complete_admin_signup')
