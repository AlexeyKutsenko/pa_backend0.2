# Generated by Django 3.0.7 on 2020-11-22 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fin', '0010_auto_20201121_0224'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='ticker',
            constraint=models.CheckConstraint(check=models.Q(price__gt=0), name='ticker_price_non_negative'),
        ),
    ]
