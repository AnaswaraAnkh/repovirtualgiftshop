from django.db import models
from Login.models import LoginTable
from User_Profile.models import *

# Create your models here.
class Shop_Table(models.Model):
    Name=models.CharField(max_length=50,blank=True,null=True)
    Owner_Name=models.CharField(max_length=50,blank=True,null=True)
    Email=models.CharField(max_length=50,blank=True,null=True)
    Phone_number=models.BigIntegerField(blank=True,null=True)
    Place=models.CharField(max_length=50,blank=True,null=True)
    Post=models.CharField(max_length=50,blank=True,null=True)
    Pin=models.IntegerField(blank=True,null=True)
    LOGINID=models.ForeignKey(LoginTable,on_delete=models.CASCADE,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return str(self.id)
    

class Category(models.Model):
    Categorytype=models.CharField(max_length=50,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)




class Product_Table(models.Model):
    Product_Name=models.CharField(max_length=50,blank=True,null=True)
    Image=models.FileField(max_length=50,null=True,blank=True)
    Categorytype = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null=True)
    Price=models.IntegerField(null=True,blank=True)
    Description=models.CharField(max_length=100,null=True,blank=True)
    Quantity=models.CharField(max_length=100,null=True,blank=True)
    Rating=models.FloatField(null=True,blank=True)
    SHOPLID=models.ForeignKey(LoginTable,on_delete=models.CASCADE,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    
class Offer_Table(models.Model):
    Offer_Title=models.CharField(max_length=50,blank=True,null=True)
    Offer_Description=models.CharField(max_length=50,blank=True,null=True)
    Offer_Percentage=models.CharField(max_length=50,blank=True,null=True)
    Start_date=models.DateField(max_length=50,blank=True,null=True)
    End_date=models.DateField(max_length=50,blank=True,null=True)
    PRODUCTID=models.ForeignKey(Product_Table,on_delete=models.CASCADE,blank=True,null=True)
    SHOPLID=models.ForeignKey(Shop_Table,on_delete=models.CASCADE,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class Order_Table(models.Model):
    PRODUCTID=models.ForeignKey(Product_Table,on_delete=models.CASCADE,blank=True,null=True)
    USERLID=models.ForeignKey(User_Table,on_delete=models.CASCADE,blank=True,null=True)
    Date=models.DateField(max_length=20,null=True,blank=True)
    Total_Amount=models.IntegerField(null=True,blank=True)
    Order_Status=models.CharField(max_length=50,blank=True,null=True)
    Payment_Status=models.CharField(max_length=50,blank=True,null=True)
    DELIVERYID=models.ForeignKey(Delivery_Table,on_delete=models.CASCADE,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class Orderitem_Table(models.Model):
    PRODUCTID=models.ForeignKey(Product_Table,on_delete=models.CASCADE,blank=True,null=True)
    Quantity=models.IntegerField(null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    OFFERID=models.ForeignKey(Offer_Table,on_delete=models.CASCADE,blank=True,null=True)
    ORDERID=models.ForeignKey(Order_Table,on_delete=models.CASCADE,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)





class Complaint_Table(models.Model):
    USERLID=models.ForeignKey(User_Table,on_delete=models.CASCADE,null=True,blank=True)
    
    Complaint=models.CharField(max_length=100,blank=True,null=True)
    Date=models.DateField(max_length=30,blank=True,null=True)
    Reply=models.CharField(max_length=50,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class Rating_Review_Table(models.Model):
    USERLID=models.ForeignKey(User_Table,on_delete=models.CASCADE,null=True,blank=True)
    PRODUCTID=models.ForeignKey(Product_Table,on_delete=models.CASCADE,null=True,blank=True)
    Rating=models.IntegerField(blank=True,null=True)
    Review=models.CharField(max_length=50,blank=True,null=True)
    Date=models.DateField(max_length=30,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)




