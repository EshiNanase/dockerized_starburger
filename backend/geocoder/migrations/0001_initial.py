# Generated by Django 3.2.15 on 2023-02-18 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=256, verbose_name='Адрес клиента')),
                ('latitude', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Широта')),
                ('longitude', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Долгота')),
            ],
        ),
    ]