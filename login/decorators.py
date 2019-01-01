from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def administrator_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='redirect_base_on_role'):
    """Checks if the user is an administrator. if not redirect to login page"""
    actual_decorator = user_passes_test(
        lambda u: u.is_superuser or u.is_administrator,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def registered_user_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='redirect_base_on_role'):
    """Checks if the user is a registered user. if not redirect to login page"""
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_registered_user and u.is_verified,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
