from django.db import models


class Contact(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=200)
    message = models.TextField()

    def get_absolute_url(self):
        return "Hey Thanks"

    def __str__(self):
        return self.full_name
