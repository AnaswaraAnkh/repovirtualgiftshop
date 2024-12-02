from itertools import product
from urllib import request
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from Shop.serializer import ComplaintSerializer
from User_Profile.models import User_Table


from .forms import AddOfferForm, AddProductForm, Addcategory, DeliveryForm, ShopRegForms, ShopupdateForms, UpdateOfferForm, UpdateProductForm  # Assuming you have a form class named ShopRegForms
from .models import Category, LoginTable, Offer_Table, Order_Table, Orderitem_Table, Product_Table, Rating_Review_Table, Shop_Table
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db import transaction



class shop_registration(View):
    def get(self, request):
        return render(request, 'Shop Registration.html')
    
    def post(self, request):
        form = ShopRegForms(request.POST)
        
        if form.is_valid():
            try:
                # Check if username already exists
                if LoginTable.objects.filter(username=request.POST['username']).exists():
                    return HttpResponse('''<script>alert("Username already exists! Please choose a different one.");window.location="/"</script>''')
                
                # Create a new user
                login_instance = LoginTable.objects.create_user(
                    user_type='Pending',
                    username=request.POST['username'],
                    password=request.POST['password']
                )
                
                # Save the shop details with reference to the created user
                reg_form = form.save(commit=False)
                reg_form.LOGINID = login_instance
                reg_form.save()

                return HttpResponse('''<script>alert("Registered successfully!");window.location="/"</script>''')
            
            except IntegrityError as e:
                # Print the exact error for debugging
                print(f"IntegrityError: {e}")
                return HttpResponse('''<script>alert("An error occurred while processing your request. Please try again.");window.location="/"</script>''')
        else:
            # Print form errors for debugging
            print("Form is not valid. Errors:", form.errors)
            return HttpResponse('''<script>alert("Form submission failed. Please check the form and try again.");window.location="/"</script>''')
        
class Shophomepage(View):
    def get(self,request):
        return render(request,"Shophomepage.html")
    
class Shop_Profile(View):
    def get(self,request):
        login_id = request.session.get("user_id")
        print("logid",login_id)
        obj = Shop_Table.objects.filter(LOGINID__id=login_id).first()
        print(obj)
        return render(request,'Shop Management.html',{'val':obj})
    def post(self,request):
        login_id = request.session.get("user_id")
        obj = Shop_Table.objects.filter(LOGINID__id=login_id).first()
        form = ShopupdateForms(request.POST,request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("successfully updated");window.location="Shop_profile/"</script>''')
        return HttpResponse('''<script>alert("Failed");window.location="Shop_profile/"</script>''')
    


    


class AddProducts(View):
    def get(self, request):
        obj = Category.objects.all()
        return render(request, 'Product.html', {'val': obj})

    def post(self, request):
        login_id = request.session.get("user_id")  # Retrieve the login ID of the shop
        print(login_id)  # Debugging: Check the login ID in the console

        # Fetch the LoginTable instance corresponding to the login_id
        try:
            shop_instance = LoginTable.objects.get(id=login_id)  # Get the LoginTable instance
        except LoginTable.DoesNotExist:
            return HttpResponse('''<script>alert("Invalid Shop Login ID!");window.location="/shop/AddProduct"</script>''')

        form = AddProductForm(request.POST, request.FILES)
        
        if form.is_valid():
            product = form.save(commit=False)  # Create a form instance without saving it yet
            product.SHOPLID = shop_instance     # Assign the LoginTable instance to the ForeignKey
            product.save()                     # Save the instance with the shop ID
            return HttpResponse('''<script>alert("Item Added");window.location="/shop/ViewProducts"</script>''')
        
        return HttpResponse('''<script>alert("Failed to add item");window.location="/shop/AddProduct"</script>''')

        
class ViewProducts(View):
    def get(self,request):
        obj = Product_Table.objects.filter(is_active=True)
        print(obj)
        return render (request,'Manage Product.html',{'val':obj})
    
class ProductEdit(View):
    def get(self, request, P_id):
        # Get the product by its ID
        obj = Product_Table.objects.get(id=P_id)

        # Get the selected category ID
        selected_category_id = obj.Categorytype.id if obj.Categorytype else None
        print("id",selected_category_id)
        categories = Category.objects.all()  # Replace `Category` with your category model name

        return render(request, "ProductEdit.html", {'val': obj, 'selected_category_id': selected_category_id, 'categories': categories})
    def post(self, request, P_id):
        # Get the product by its ID
        obj = Product_Table.objects.get(id=P_id)

        # Create the form with POST data and any uploaded files
        form = UpdateProductForm(request.POST, request.FILES, instance=obj)

        # Check if the form is valid
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("Successfully updated");window.location="/shop/ViewProducts"</script>''')
        
        return HttpResponse('''<script>alert("Failed to update");window.location="/shop/EditItem"</script>''')


class ProductDelete(View):
    def get(self,request,P_id):
        obj=Product_Table.objects.get(id=P_id)
        obj.is_active=False
        obj.save()
        return HttpResponse('''<script>alert("successfully deleted");window.location="/shop/ViewProducts"</script>''')
    
class AddCategory(View):
    def get(self,request):
        return render(request,"Add category.html")
    def post(self,request):
        form=Addcategory(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("Category Added");window.location="/shop/AddCategory"</script>''')
        return HttpResponse('''<script>alert("Failed");window.location="/"</script>''')


    

class ViewOffer(View):
 def get(self,request):
     obj=Offer_Table.objects.filter(is_active=True)
     return render(request,"Manage Offer.html",{'val':obj})
 
class AddOffer(View):
    def get(self, request):
        # Fetch all products to display in the dropdown
        obj = Product_Table.objects.all()
        return render(request, "Offer.html", {'val': obj})

    def post(self, request):
        product_id = request.POST.get("product")  # Get the selected product ID from the form
        if product_id:  # Ensure a product is selected
            try:
                # Fetch the selected product
                product = Product_Table.objects.get(id=product_id)
                
                # Create the offer using the form data
                form = AddOfferForm(request.POST)
                if form.is_valid():
                    offer = form.save(commit=False)  # Save the form without committing to the database
                    offer.PRODUCTID = product  # Associate the offer with the selected product
                    offer.save()  # Save the offer to the database
                    return HttpResponse(
                        '''<script>alert("Offer Added");window.location="/shop/ViewOffer"</script>'''
                    )
                else:
                    return HttpResponse(
                        '''<script>alert("Form validation failed");window.location="/"</script>'''
                    )
            except Product_Table.DoesNotExist:
                return HttpResponse(
                    '''<script>alert("Product not found");window.location="/"</script>'''
                )
        else:
            return HttpResponse(
                '''<script>alert("No product selected");window.location="/"</script>'''
            )

 
class OfferEdit(View):
    def get(self,request,O_id):
        obj=Offer_Table.objects.get(id=O_id)
        return render(request,"OfferEdit.html",{'val':obj})
    def post(self,request,O_id):
        obj = Offer_Table.objects.get(id=O_id)
        form = UpdateOfferForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("successfully updated");window.location="/shop/ViewOffer"</script>''')
        return HttpResponse('''<script>alert("Failed");window.location="/EditItem"</script>''')
    
class OfferDelete(View):
    def get(self,request,O_id):
        obj=Offer_Table.objects.get(id=O_id)
        obj.is_active=False
        obj.save()
        return HttpResponse('''<script>alert("successfully deleted");window.location="/shop/ViewOffer"</script>''')
    
from django.shortcuts import render
from django.views import View
from .models import Order_Table, Orderitem_Table

class CustomerOrders(View):
    def get(self, request):
        # Fetch the logged-in shop owner ID
        login_id = request.session.get("user_id")
        print("Shop Owner ID:", login_id)

        # Fetch orders where the shop owner's product is involved
        orders = Order_Table.objects.filter(PRODUCTID__SHOPLID=login_id).all()

        # Fetch the corresponding order items
        order_items = Orderitem_Table.objects.filter(ORDERID__in=orders)

        # Calculate total amount for each order item
        for item in order_items:
            item.total_amount = item.Quantity * item.Price

        # Render the orders in the template
        return render(request, 'View Orders.html', {"order_items": order_items})


class UploadDeliverystatus(View):
    def get(self,request):
        return render(request,'Upload Delivery Details.html')
    def post(self,request):
        form=DeliveryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("Details Upload");window.location="UploadDeliverystatus"</script>''')
        return HttpResponse('''<script>alert("Failed");window.location="/"</script>''')
    

class Rating_Review(View):
    def get(self, request):
        # Get the shop owner's login ID from the session
        login_id = request.session.get("user_id")
        print("Shop Owner ID:", login_id)

        # Fetch reviews for the products added by this shop owner
        reviews = Rating_Review_Table.objects.filter(PRODUCTID__SHOPLID=login_id).select_related('USERLID', 'PRODUCTID')

        # Debug print to verify the fetched reviews
        print("Reviews:", reviews)

        # Render the reviews in the template
        return render(request, 'View Review.html', {'reviews': reviews})
    

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Complaint_Table


# POST: Submit a complaint
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Complaint_Table

from datetime import date

class SubmitComplaintView(APIView):
    def post(self, request, user_id):
        # Prepare the data for insertion
        data = request.data.copy()
        print(data)
        data['USERLID'] = user_id
        data['Date'] = date.today()  # Automatically set the current date
        data['is_active'] = True  # Ensure is_active is set to True
        
        # Log the data for debugging
        print(f"Data being saved: {data}")

        # Validate and save the complaint
        serializer = ComplaintSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# GET: Fetch complaints for a specific user
class FetchComplaintsView(APIView):
    def get(self, request, user_id):
        complaints = Complaint_Table.objects.filter(USERLID=user_id)
        serializer = ComplaintSerializer(complaints, many=True)
        return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
    

