from django.db import models

from Login.models import LoginTable



# Create your models here.
class User_Table(models.Model):
    First_Name=models.CharField(max_length=50,blank=True,null=True)
    Last_Name=models.CharField(max_length=50,blank=True,null=True)
    Address=models.CharField(max_length=50,blank=True,null=True)
    City=models.CharField(max_length=50,blank=True,null=True)
    District=models.CharField(max_length=50,blank=True,null=True)
    Pincode=models.IntegerField(blank=True,null=True)
    Phone_Number=models.BigIntegerField(blank=True,null=True)
    Email=models.CharField(max_length=50,blank=True,null=True)
    LOGINID=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)
    profileimage=models.FileField(upload_to='profileimages',null=True,blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class Delivery_Table(models.Model):
    Customer_Name=models.CharField(max_length=50,blank=True,null=True)
    ProductName=models.CharField(max_length=50,blank=True,null=True)
    Location=models.CharField(max_length=50,blank=True,null=True)
    Phone_Number=models.BigIntegerField(blank=True,null=True)
    Delivery_Date=models.DateField(max_length=30,blank=True,null=True)
    Status=models.CharField(max_length=50,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)



class Chatbot_Table(models.Model):
    Senderid=models.IntegerField(blank=True,null=True)
    Receiverid=models.IntegerField(blank=True,null=True)
    Msg=models.CharField(max_length=50,blank=True,null=True)
    Date=models.DateField(max_length=30,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class Wallet(models.Model):
    USERID = models.ForeignKey(User_Table, on_delete=models.CASCADE, related_name='wallet')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    