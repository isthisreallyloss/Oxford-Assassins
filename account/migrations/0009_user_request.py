# Generated by Django 4.0.3 on 2022-07-25 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_remove_user_registered_user_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='request',
            field=models.BooleanField(default=False, verbose_name='request paymment'),
        ),
    ]
