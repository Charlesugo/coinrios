from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from login.models import User
from login.forms import RegisteredUserSignUpForm


class RegisteredUserSignUpView(CreateView):
    model = User
    form_class = RegisteredUserSignUpForm
    # success_url = reverse_lazy("registered_user:dashboard")
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Registered User'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        if self.request.method == "POST":
            form = RegisteredUserSignUpForm(self.request.POST, self.request.FILES)
            if form.is_valid():
                # check_form = form.save(commit=False)
                form.save()
                return redirect('registered_user:dashboard')
            else:
                # request.session['wrong_file_or_size'] = True
                # request.session['wrong_file_or_size'].set_expiry(5)

                args = {}
                return redirect('create_registered_user')

    #     user = form.save()
    #     # login(self.request, user)
    #     return redirect('registered_user:dashboard')


"2216133060"

