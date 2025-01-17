# Generated by Django 4.2.15 on 2024-09-12 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_Profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatbot_table',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='delivery_table',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user_table',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
