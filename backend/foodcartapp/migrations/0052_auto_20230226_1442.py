# Generated by Django 3.2.15 on 2023-02-26 11:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0051_alter_order_restaurant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='contact_time',
            new_name='contacted_at',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='delivery_time',
            new_name='delivered_at',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='register_time',
            new_name='registered_at',
        ),
        migrations.RemoveField(
            model_name='order',
            name='restaurant',
        ),
        migrations.AddField(
            model_name='order',
            name='cooking_restaurant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='restaurant', to='foodcartapp.restaurant', verbose_name='Ресторан'),
        ),
        migrations.AlterField(
            model_name='order',
            name='comment',
            field=models.TextField(blank=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.CharField(blank=True, choices=[('Cash', 'Наличность'), ('Card', 'Карта')], db_index=True, max_length=256, verbose_name='Оплата'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='foodcartapp.product', verbose_name='Товар'),
        ),
    ]
