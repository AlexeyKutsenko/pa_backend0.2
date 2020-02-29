# Generated by Django 3.0.3 on 2020-02-10 03:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fin', '0002_auto_20200209_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('coefficient', models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MinValueValidator(1e-06), django.core.validators.MaxValueValidator(1)])),
                ('current_money_amount', models.DecimalField(decimal_places=2, max_digits=19)),
                ('target_money_amount', models.DecimalField(decimal_places=2, max_digits=19)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='ticker',
            name='weight',
            field=models.DecimalField(decimal_places=10, max_digits=12, validators=[django.core.validators.MinValueValidator(1e-06), django.core.validators.MaxValueValidator(1)]),
        ),
    ]