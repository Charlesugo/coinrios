from django.db import models
from django.contrib.auth.models import AbstractUser

from login.validators import validate_file_size


class User(AbstractUser):
    is_administrator = models.BooleanField(default=False)
    is_registered_user = models.BooleanField(default=False)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    is_verified = models.BooleanField(default=False)
    confirmed_email = models.BooleanField(default=False)
    drivers_license_or_international_passport_or_national_id_card = models.FileField(validators=[validate_file_size])
    utility_bill = models.FileField(validators=[validate_file_size])


