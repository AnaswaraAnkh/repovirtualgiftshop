from django.forms import ModelForm

from Shop.models import Category, Offer_Table, Product_Table, Shop_Table
from User_Profile.models import Delivery_Table


class ShopRegForms(ModelForm):
    class Meta:
        model=Shop_Table
        fields=['Name','Owner_Name','Email','Phone_number','Place','Post','Pin']


class Addcategory(ModelForm):
    class Meta:
        model=Category
        fields=['Categorytype']

class ShopupdateForms(ModelForm):
    class Meta:
        model=Shop_Table
        fields=['Name','Owner_Name','Email','Phone_number','Place','Post','Pin']

class AddProductForm(ModelForm):
    class Meta:
        model=Product_Table
        fields=['Product_Name','Image','Categorytype','Price','Description','Quantity']

class UpdateProductForm(ModelForm):
    class Meta:
        model=Product_Table
        fields=['Product_Name','Image','Categorytype','Price','Description','Quantity']

class AddOfferForm(ModelForm):
    class Meta:
        model=Offer_Table
        fields=['Offer_Title','Offer_Description','Offer_Percentage','Start_date','End_date']

class UpdateOfferForm(ModelForm):
    class Meta:
        model=Offer_Table
        fields=['Offer_Title','Offer_Description','Offer_Percentage','Start_date','End_date']

class DeliveryForm(ModelForm):
    class Meta:
        model=Delivery_Table
        fields=['Customer_Name','ProductName','Location','Phone_Number','Delivery_Date','Status']
        



        
