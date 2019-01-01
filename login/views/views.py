from django.http import HttpResponse
from django.shortcuts import redirect, reverse
from django.views.generic import TemplateView


class CreateWhichUser(TemplateView):
    template_name = 'registration/signup.html'


def redirect_base_on_role(request):
    if request.user.is_authenticated:
        if request.user.is_registered_user:
            if request.user.is_verified:
                return redirect('registered_user:dashboard')
            else:
                return redirect('crypto:verification_process')
        else:
            return redirect('administrator:adminDashboard')
    else:
        return redirect('crypto:landingPage')
