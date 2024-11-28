from rest_framework.serializers import ModelSerializer,FileField,SerializerMethodField

from User_Profile.models import Delivery_Table, User_Table, Wallet
from Login.models import LoginTable
from Shop.models import Category, Offer_Table, Order_Table, Orderitem_Table, Product_Table, Rating_Review_Table, Shop_Table


class UserSerializer(ModelSerializer):
    class Meta:
        model = User_Table
        fields = ['First_Name', 'Last_Name', 'Address', 'City', 'District',  'Pincode', 'Phone_Number','Email','profileimage']

class LoginSerializer(ModelSerializer):
    class Meta:
        model=LoginTable
        fields=['username']

class UserTableSerializer(ModelSerializer):
    profileimage =FileField(use_url=True) 
    class Meta:
        model = User_Table
        fields = '__all__' 

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = [ 'Categorytype' ]



class OfferSerializer(ModelSerializer):
    class Meta:
        model = Offer_Table
        fields = [
            'Offer_Title', 'Offer_Description', 'Offer_Percentage',
            'Start_date', 'End_date']



class ProductSerializer1(ModelSerializer):
    offers = OfferSerializer(source='offer_table_set', many=True, read_only=True)
    category_name = SerializerMethodField()
    shop_name = SerializerMethodField()  # Add a SerializerMethodField for shop name

    class Meta:
        model = Product_Table
        fields = [
            'id','Product_Name', 'Image', 'Categorytype', 'Price',
            'Description', 'Quantity', 'SHOPLID', 'offers',
            'category_name', 'shop_name','Rating'  # Include shop_name in the fields
        ]

    def get_category_name(self, obj):
        if obj.Categorytype:
            return obj.Categorytype.Categorytype  # Assuming `Categorytype` has a field named `Categorytype`
        return None

    def get_shop_name(self, obj):
        # Navigate the relationship chain to fetch the shop name
        if obj.SHOPLID:
            shop = Shop_Table.objects.filter(LOGINID=obj.SHOPLID).first()
            if shop:
                return shop.Name
        return None



class WalletSerializer(ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['balance']



class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = Orderitem_Table
        fields = [ 'Quantity', 'Price', 'OFFERID', 'ORDERID']

class DeliverySerializer(ModelSerializer):
    class Meta:
        model = Delivery_Table
        fields = ['Customer_Name', 'ProductName', 'Location', 'Phone_Number', 'Delivery_Date', 'Status']

from rest_framework import serializers

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order_Table
        fields = [
            
            'Date', 
            'Total_Amount', 
            'Order_Status', 
            'Payment_Status', 
            
        ]

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating_Review_Table
        fields = ['USERLID', 'PRODUCTID', 'Rating', 'Review','Date']


class ReviewSerializerview(serializers.ModelSerializer):
    product_name = serializers.CharField(source='PRODUCTID.Product_name', read_only=True)  # Assuming `product_name` is the field in Product_Table
    username = serializers.CharField(source='USERLID.username', read_only=True)  # Assuming `username` is the field in User_Table

    class Meta:
        model = Rating_Review_Table
        fields = ['product_name', 'username', 'Rating', 'Review', 'Date', 'created_at', 'updated_at']
