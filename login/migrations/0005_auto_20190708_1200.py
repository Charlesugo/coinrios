# Generated by Django 2.2.2 on 2019-07-08 11:00

from django.db import migrations, models
import login.validators


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20181211_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='confirmed_email',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='drivers_license_or_international_passport_or_national_id_card',
            field=models.FileField(upload_to='', validators=[login.validators.validate_file_size]),
        ),
        migrations.AlterField(
            model_name='user',
            name='utility_bill',
            field=models.FileField(upload_to='', validators=[login.validators.validate_file_size]),
        ),
    ]
