# Generated by Django 4.2.3 on 2023-07-07 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency_exchange', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchangerate',
            name='rate',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
    ]