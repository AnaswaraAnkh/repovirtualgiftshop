# Generated by Django 4.2.15 on 2024-11-23 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0010_alter_logintable_status_alter_logintable_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logintable',
            name='user_type',
            field=models.CharField(choices=[('USER', 'user'), ('Admin', 'admin'), ('Pending', 'pending'), ('Shop', 'shop')], max_length=20, null=True),
        ),
    ]
