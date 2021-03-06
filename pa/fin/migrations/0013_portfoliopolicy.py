# Generated by Django 3.1.3 on 2020-11-26 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fin', '0012_auto_20201123_0328'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('asset_to_equity_max_ratio', models.DecimalField(decimal_places=2, default=0, max_digits=19)),
                ('asset_to_equity_min_ratio', models.DecimalField(decimal_places=2, default=0, max_digits=19)),
                ('debt_to_equity_max_ratio', models.DecimalField(decimal_places=2, default=0, max_digits=19)),
                ('max_dividend_payout_ratio', models.DecimalField(decimal_places=2, default=0, max_digits=19)),
                ('minimum_annual_earnings_growth', models.DecimalField(decimal_places=2, default=0, max_digits=19)),
                ('pe_quantile', models.IntegerField(default=50)),
                ('portfolio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='portfolio_policy', to='fin.portfolio')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
