# Generated by Django 4.0.3 on 2022-07-17 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_assassin_user_assassin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='assassin',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.assassin'),
        ),
    ]
