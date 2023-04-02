# Generated by Django 3.2.15 on 2023-02-18 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0040_alter_orderitem_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='Количество'),
        ),
    ]