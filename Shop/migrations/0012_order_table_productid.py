# Generated by Django 4.2.15 on 2024-11-30 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0011_remove_order_table_shoplid'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_table',
            name='PRODUCTID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Shop.product_table'),
        ),
    ]