# Generated by Django 3.2.15 on 2023-02-26 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geocoder', '0007_auto_20230226_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='bad_address',
            field=models.BooleanField(default=False, verbose_name='Рабочий ли адресс'),
        ),
    ]