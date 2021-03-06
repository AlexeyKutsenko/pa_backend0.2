# Generated by Django 3.0.4 on 2020-05-11 21:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticker',
            old_name='name',
            new_name='symbol',
        ),
        migrations.AddField(
            model_name='ticker',
            name='company',
            field=models.CharField(default='Unknown', max_length=50),
        ),
        migrations.AlterField(
            model_name='index',
            name='data_source_url',
            field=models.URLField(choices=[('https://www.slickcharts.com/sp500', 'S&P 500'), ('https://www.slickcharts.com/nasdaq100', 'NASDAQ 100'), ('https://www.ishares.com/us/products/239516/ishares-us-medical-devices-etf/1467271812596.ajax', 'IHI')], unique=True),
        ),
        migrations.AlterField(
            model_name='ticker',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=19, validators=[django.core.validators.MinValueValidator(1e-06), django.core.validators.MaxValueValidator(1.000001)]),
        ),
    ]
