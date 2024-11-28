# Generated by Django 4.2.15 on 2024-11-28 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0016_alter_logintable_status_alter_logintable_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logintable',
            name='status',
            field=models.CharField(choices=[('DEACTIVE', 'Inactive'), ('ACTIVE', 'Active')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='logintable',
            name='user_type',
            field=models.CharField(choices=[('Shop', 'shop'), ('Admin', 'admin'), ('Pending', 'pending'), ('USER', 'user')], max_length=20, null=True),
        ),
    ]
