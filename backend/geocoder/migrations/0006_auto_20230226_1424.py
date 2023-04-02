# Generated by Django 3.2.15 on 2023-02-26 11:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('geocoder', '0005_auto_20230219_0157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=256, unique=True, verbose_name='Адрес')),
                ('latitude', models.DecimalField(decimal_places=15, default=0, max_digits=30, verbose_name='Широта')),
                ('longitude', models.DecimalField(decimal_places=15, default=0, max_digits=30, verbose_name='Долгота')),
                ('filled_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
        migrations.DeleteModel(
            name='AddressClient',
        ),
        migrations.DeleteModel(
            name='AddressRestaurant',
        ),
    ]
