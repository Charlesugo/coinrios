# Generated by Django 2.2.2 on 2019-07-08 11:00

from django.db import migrations, models
import login.validators


class Migration(migrations.Migration):

    dependencies = [
        ('registered_user', '0005_sellbitcoin_sellethereum_sellperfectmoney_sellripple'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completeuserregistration',
            name='KYC',
            field=models.FileField(upload_to='', validators=[login.validators.validate_file_size]),
        ),
    ]
