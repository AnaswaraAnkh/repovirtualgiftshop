# Generated by Django 4.2.15 on 2024-09-05 09:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('User_Profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Offer_Title', models.CharField(blank=True, max_length=50, null=True)),
                ('Offer_Description', models.CharField(blank=True, max_length=50, null=True)),
                ('Offer_Percentage', models.CharField(blank=True, max_length=50, null=True)),
                ('Start_date', models.DateField(blank=True, max_length=50, null=True)),
                ('End_date', models.DateField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(blank=True, max_length=20, null=True)),
                ('Total_Amount', models.IntegerField(blank=True, null=True)),
                ('Order_Status', models.CharField(blank=True, max_length=50, null=True)),
                ('Payment_Status', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('DELIVERYID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='User_Profile.delivery_table')),
            ],
        ),
        migrations.CreateModel(
            name='Shop_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Owner_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Email', models.CharField(blank=True, max_length=50, null=True)),
                ('Phone_number', models.BigIntegerField(blank=True, null=True)),
                ('Place', models.CharField(blank=True, max_length=50, null=True)),
                ('Post', models.CharField(blank=True, max_length=50, null=True)),
                ('Pin', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('LOGINID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating_Review_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rating', models.IntegerField(blank=True, null=True)),
                ('Review', models.CharField(blank=True, max_length=50, null=True)),
                ('Date', models.DateField(blank=True, max_length=30, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('SHOPLID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Shop.shop_table')),
                ('USERLID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='User_Profile.user_table')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Image', models.FileField(blank=True, max_length=50, null=True, upload_to='')),
                ('Category', models.CharField(blank=True, max_length=50, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('Description', models.CharField(blank=True, max_length=100, null=True)),
                ('Quantity', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('SHOPLID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Shop.shop_table')),
            ],
        ),
        migrations.CreateModel(
            name='Orderitem_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField(blank=True, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('OFFERID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Shop.offer_table')),
                ('ORDERID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Shop.order_table')),
                ('PRODUCTID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Shop.product_table')),
            ],
        ),
        migrations.AddField(
            model_name='order_table',
            name='SHOPLID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Shop.shop_table'),
        ),
        migrations.AddField(
            model_name='order_table',
            name='USERLID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='User_Profile.user_table'),
        ),
        migrations.AddField(
            model_name='offer_table',
            name='PRODUCTID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Shop.product_table'),
        ),
        migrations.AddField(
            model_name='offer_table',
            name='SHOPLID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Shop.shop_table'),
        ),
        migrations.CreateModel(
            name='Complaint_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Complaint', models.CharField(blank=True, max_length=50, null=True)),
                ('Date', models.DateField(blank=True, max_length=30, null=True)),
                ('Reply', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('SHOPLID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Shop.shop_table')),
                ('USERLID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='User_Profile.user_table')),
            ],
        ),
    ]