# Generated by Django 4.2.15 on 2024-11-29 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0010_alter_product_table_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_table',
            name='SHOPLID',
        ),
    ]
