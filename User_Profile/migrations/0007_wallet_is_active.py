# Generated by Django 4.2.15 on 2024-11-23 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_Profile', '0006_wallet'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
