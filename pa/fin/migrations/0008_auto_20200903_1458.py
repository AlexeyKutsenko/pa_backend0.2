# Generated by Django 3.0.7 on 2020-09-03 14:58

from django.db import migrations, models
import django.db.models.manager
import fin.models.ticker.ticker


class Migration(migrations.Migration):

    dependencies = [
        ('fin', '0007_tickerstatement'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='ticker',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('outdated_tickers', fin.models.ticker.ticker.OutdatedTickersManager()),
            ],
        ),
        migrations.AlterField(
            model_name='index',
            name='data_source_url',
            field=models.URLField(choices=[('https://www.slickcharts.com/sp500', 'S&P 500'), ('https://www.slickcharts.com/nasdaq100', 'NASDAQ 100'), ('https://www.ishares.com/us/products/239516/ishares-us-medical-devices-etf/1467271812596.ajax', 'IHI'), ('https://www.ishares.com/us/products/239714/ishares-russell-3000-etf/1467271812596.ajax', 'RUSSEL3000'), ('https://www.ishares.com/us/products/239705/ishares-phlx-semiconductor-etf/1467271812596.ajax', 'SOXX')], unique=True),
        ),
        migrations.AlterField(
            model_name='ticker',
            name='company_name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
    ]
