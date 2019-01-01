# Generated by Django 2.1.2 on 2018-12-06 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
        ('registered_user', '0003_auto_20181204_1037'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompleteUserRegistration',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('KYC', models.FileField(upload_to='')),
            ],
        ),
    ]
