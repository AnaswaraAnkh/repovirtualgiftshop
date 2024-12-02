from decimal import Decimal
import decimal
from django.shortcuts import get_object_or_404, render
from django.views import View
from rest_framework.views import APIView

from User_Profile.serializer import CategorySerializer, DeliverySerializer, LoginSerializer, OrderItemSerializer, OrderSerializer, ProductSerializer1,ReviewSerializerview, UserSerializer, UserTableSerializer
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status

from Login.models import LoginTable
from User_Profile.models import User_Table
from Shop.models import Category, Offer_Table, Order_Table, Orderitem_Table, Product_Table, Rating_Review_Table

# Create your views here.
# class UserReg(APIView):
#     def post(self, request):
#         print("###############",request.data)
#         user_serial = UserSerializer(data=request.data)
#         login_serial = LoginSerializer(data=request.data)
#         data_valid = user_serial.is_valid()
#         login_valid = login_serial.is_valid()

#         if data_valid and login_valid:
#             hashed_password = make_password(request.data['password'])
#             login_profile = login_serial.save(user_type='USER',password=hashed_password, status='Active')
#             user_serial.save(LOGINID=login_profile)
#                 # Include a success message in the response
#             response_data = {
#                 'message': 'success',
#                 'data': user_serial.data  # Include the serialized user data if needed
#             }
#             return Response(response_data, status=status.HTTP_200_OK)
#         return Response({'login_error': login_serial.errors if not login_valid else None,
#                          'user_error': user_serial.errors if not data_valid else None}, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from .models import Delivery_Table, Wallet  # Import the Wallet model


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from .models import Wallet


class UserReg(APIView):
    def post(self, request):
        print("############### Request Data:", request.data)  # Inspect incoming data
        user_serial = UserSerializer(data=request.data)
        login_serial = LoginSerializer(data=request.data)

        # Validate serializers
        data_valid = user_serial.is_valid()
        login_valid = login_serial.is_valid()

      
     

        if data_valid and login_valid:
            hashed_password = make_password(request.data['password'])
            login_profile = login_serial.save(user_type='USER', password=hashed_password, status='Active')
            user = user_serial.save(LOGINID=login_profile)

            # Create a Wallet for the user with default balance
            Wallet.objects.create(USERID=user, balance=1000.00)

            # Success response
            response_data = {
                'message': 'success',
                'data': user_serial.data
            }
            return Response(response_data, status=status.HTTP_200_OK)

        # Return errors in response for debugging
        return Response({
            'login_error': login_serial.errors if not login_valid else None,
            'user_error': user_serial.errors if not data_valid else None
        }, status=status.HTTP_400_BAD_REQUEST)

    

from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST,HTTP_401_UNAUTHORIZED


from django.contrib.auth.hashers import check_password

# class LoginPage(APIView):
#     def post(self, request):
#         response_dict = {}

#         # Get data from the request
#         username = request.data.get("username")
#         password = request.data.get("password")
        
#         # Validate input
#         if not username or not password:
#             response_dict["message"] = "failed"
#             return Response(response_dict, status=HTTP_400_BAD_REQUEST)

#         # Fetch the user from LoginTable
#         t_user = LoginTable.objects.filter(username=username).first()

#         if not t_user:
#             response_dict["message"] = "failed"
#             return Response(response_dict, status=HTTP_401_UNAUTHORIZED)

#         # Check password using `check_password`
#         if not check_password(password, t_user.password):
#             response_dict["message"] = "failed"
#             return Response(response_dict, status=HTTP_401_UNAUTHORIZED)

#         # Successful login response
#         response_dict["message"] = "success"
#         response_dict["user_id"] = t_user.id  
#         response_dict["Address"] = t_user.Address
#         response_dict["City"] = t_user.City
#         response_dict["District"] = t_user.District
#         response_dict["Pincode"] = t_user.Pincode
#         response_dict["Phone_Number"] = t_user.Phone_Number
#         # Include user-specific details as needed
#         return Response(response_dict, status=HTTP_200_OK)


class LoginPage(APIView):
    def post(self, request):
        response_dict = {}

        # Get data from the request
        username = request.data.get("username")
        password = request.data.get("password")
        
        # Validate input
        if not username or not password:
            response_dict["message"] = "failed"
            return Response(response_dict, status=HTTP_400_BAD_REQUEST)

        # Fetch the user from LoginTable
        t_user = LoginTable.objects.filter(username=username).first()

        if not t_user:
            response_dict["message"] = "failed"
            return Response(response_dict, status=HTTP_401_UNAUTHORIZED)

        # Check password using `check_password`
        if not check_password(password, t_user.password):
            response_dict["message"] = "failed"
            return Response(response_dict, status=HTTP_401_UNAUTHORIZED)

        # Fetch additional user details from User_Table
        user_details = User_Table.objects.filter(LOGINID=t_user).first()

        # Successful login response
        response_dict["message"] = "success"
        response_dict["login_id"] = t_user.id  

        # Include user-specific details if available
        if user_details:
            response_dict["id"] = user_details.id
            response_dict["Full_Name"] = f"{user_details.First_Name} {user_details.Last_Name}".strip()
            response_dict["Address"] = user_details.Address
            response_dict["City"] = user_details.City
            response_dict["District"] = user_details.District
            response_dict["Pincode"] = user_details.Pincode
            response_dict["Phone_Number"] = user_details.Phone_Number
            response_dict["profileImage"] = user_details.profileimage.url
        else:
            # Default values if user details are not found
            response_dict["First_Name"] = None
            response_dict["Last_Name"] = None
            response_dict["Address"] = None
            response_dict["City"] = None
            response_dict["District"] = None
            response_dict["Pincode"] = None
            response_dict["Phone_Number"] = None
            response_dict["profileimage"] = None

        # # Fetch product details (assumes a Product_Table related to the user or login)
        # product_details = Product_Table.objects.filter(SHOPLID=user_details).first()

        # if product_details:
        #     response_dict["id"] = product_details.id
        #     response_dict["Product_Name"] = product_details.Product_Name
        # else:
        #     # Default product details if not found
        #     response_dict["product_id"] = None
        #     response_dict["product_name"] = None

        return Response(response_dict, status=HTTP_200_OK)


class UserProfileView(APIView):
    """
    API View to retrieve a user's profile.
    """
    def get(self, request,id):
        try:
            # Get the user from the request (assuming authentication is implemented)
            
            # Fetch the associated user profile
            user_profile = User_Table.objects.filter(LOGINID__id=id).first()
            print("sdfg",user_profile)

            
            if not user_profile:
                return Response(
                    {"message": "Profile not found for the logged-in user."},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            # Serialize the profile data
            serialized_data = UserTableSerializer(user_profile).data
            print(serialized_data)
            
            # Return the profile data
            return Response(
                serialized_data,
                status=status.HTTP_200_OK
            )
        
        except Exception as e:
            return Response(
                {"message": "An error occurred while retrieving the profile.", "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    def put(self, request,id):
            """
            Update user profile details.
            """
            try:
                # Get the profile ID from the request data
    
                # Fetch the profile object
                user_profile = User_Table.objects.filter(LOGINID__id=id).first()
                print(user_profile)
                
                if not user_profile:
                    return Response(
                        {"message": "Profile not found."},
                        status=status.HTTP_404_NOT_FOUND
                    )
                
                # Deserialize and validate the input data
                serializer = UserTableSerializer(user_profile, data=request.data, partial=True)
                
                if serializer.is_valid():
                    # Save the updated profile
                    serializer.save()
                    return Response(
                        {"message": "Profile updated successfully.", "data": serializer.data},
                        status=status.HTTP_200_OK
                    )
                
                # Return validation errors
                return Response(
                    {"message": "Validation failed.", "errors": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            except Exception as e:
                return Response(
                    {"message": "An error occurred while updating the profile.", "error": str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            
class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ProductWithOffersView1(APIView):
    def get(self, request):
        products = Product_Table.objects.all()
        serializer = ProductSerializer1(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    




class WalletBalanceAPIView(APIView):
    def get(self, request, id):
        try:
            # Fetch the user by id
            user_details = User_Table.objects.filter(id=id).first()
            
            if not user_details:
                return Response({"error": "User details not found"}, status=status.HTTP_404_NOT_FOUND)

            # Fetch the wallet for this user
            wallet = Wallet.objects.filter(USERID=user_details).first()

            if not wallet:
                return Response({"error": "Wallet not found for this user"}, status=status.HTTP_404_NOT_FOUND)

            # Return the wallet balance
            return Response({
                "message": "Success",
                "wallet_balance": wallet.balance
            }, status=status.HTTP_200_OK)

        except Exception as e:
            # Log the error and return a server error response
            print(f"Error occurred: {str(e)}")
            return Response({"error": "An error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED,HTTP_500_INTERNAL_SERVER_ERROR

class UpdateProfileImage(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, id):
        response_dict = {}

        # Use the `id` from the URL to fetch the user record
        try:
            user = User_Table.objects.filter(LOGINID_id=id).first()
            if not user:
                response_dict["message"] = "failed"
                response_dict["error"] = "User not found."
                return Response(response_dict, status=HTTP_401_UNAUTHORIZED)
        except Exception as e:
            response_dict["message"] = "failed"
            response_dict["error"] = f"Database error: {str(e)}"
            return Response(response_dict, status=HTTP_500_INTERNAL_SERVER_ERROR)

        # Check for the uploaded file
        if "profileimage" not in request.FILES:
            response_dict["message"] = "failed"
            response_dict["error"] = "No image file provided."
            return Response(response_dict, status=HTTP_400_BAD_REQUEST)

        # Update the profile image
        try:
            profile_image = request.FILES["profileimage"]
            user.profileimage = profile_image
            user.save()

            response_dict["message"] = "success"
            response_dict["profileImage"] = user.profileimage.url if user.profileimage else None
            return Response(response_dict, status=HTTP_200_OK)

        except Exception as e:
            response_dict["message"] = "failed"
            response_dict["error"] = f"Error updating profile image: {str(e)}"
            return Response(response_dict, status=HTTP_500_INTERNAL_SERVER_ERROR)
        


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import date



class PlaceOrderView(APIView):
    def post(self, request, user_id):
        try:
            # Fetch the user
            user = User_Table.objects.filter(id=user_id).first()
            if not user:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

            # Extract cart items and delivery details from request data
            cart_items = request.data.get("cart_items")  # List of cart items
            delivery_details = request.data.get("delivery_details")  # Delivery details as a dict
            total_amount = request.data.get("total_Amount")

            if not cart_items or not delivery_details or total_amount is None:
                return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)

            # Validate delivery details
            required_fields = ["name", "address", "city", "district", "pincode", "phone"]
            if not all(field in delivery_details for field in required_fields):
                return Response({"error": "Incomplete delivery details"}, status=status.HTTP_400_BAD_REQUEST)

            # Check user's wallet balance
            wallet = Wallet.objects.filter(USERID=user).first()
            if not wallet:
             return Response({"error": "User wallet not found"}, status=status.HTTP_404_NOT_FOUND)

            if wallet.balance < Decimal(total_amount):
             return Response({"error": "Insufficient wallet balance"}, status=status.HTTP_400_BAD_REQUEST)

            wallet.balance -= Decimal(total_amount)  # Convert total_amount to Decimal
            wallet.save()

            # Create Delivery Record
            delivery = Delivery_Table.objects.create(
                Customer_Name=delivery_details["name"],
                ProductName=", ".join([item["Product_Name"] for item in cart_items]),
                Location=f"{delivery_details['address']}, {delivery_details['city']}, {delivery_details['district']}",
                Phone_Number=delivery_details["phone"],
                Delivery_Date=date.today(),
                Status="Pending"
            )

            # Create Order
            order = Order_Table.objects.create(
                USERLID=user,
                Date=date.today(),
                Total_Amount=total_amount,
                Order_Status="Pending",
                Payment_Status="Paid",  # Set payment status as paid since the wallet is charged
                DELIVERYID=delivery  # Link the delivery record
            )

            # Process Cart Items and Create Order Items
            for item in cart_items:
                product = Product_Table.objects.filter(Product_Name=item["Product_Name"]).first()
                if not product:
                    return Response({"error": f"Product '{item['Product_Name']}' not found"}, status=status.HTTP_404_NOT_FOUND)

                # Fetch offer if present
                offer = None
                if item.get("Offer"):
                    offer_data = item["Offer"]
                    offer = Offer_Table.objects.filter(Offer_Title=offer_data["Offer_Title"]).first()
                    if not offer:
                        return Response({"error": f"Offer '{offer_data['Offer_Title']}' not found"},
                                        status=status.HTTP_404_NOT_FOUND)

                # Create Order Item
                Orderitem_Table.objects.create(
                    PRODUCTID=product,
                    Quantity=item["Quantity"],
                    Price=item["DiscountedPrice"],  # Use discounted price if offer is applied
                    OFFERID=offer,
                    ORDERID=order
                )

            return Response({
                "message": "Order placed successfully",
                "order_id": order.id,
                "remaining_balance": wallet.balance
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class OrderHistoryView(APIView):
    def get(self, request, user_id):
        try:
            # Fetch orders for the specific user
            orders = Order_Table.objects.filter(USERLID_id=user_id, is_active=True).order_by("-created_at")
            if not orders.exists():
                return Response({"message": "No order history found for this user"}, status=status.HTTP_404_NOT_FOUND)

            order_history = []

            for order in orders:
                # Fetch related order items for the order
                order_items = Orderitem_Table.objects.filter(ORDERID=order, is_active=True)

                order_data = {
                    "OrderID": order.id,
                    "Date": order.Date,
                    "Total_Amount": order.Total_Amount,
                    "Order_Status": order.Order_Status,
                    "Payment_Status": order.Payment_Status,
                    "DeliveryID": order.DELIVERYID.id if order.DELIVERYID else None,
                    "OrderItems": [
                        {
                            "ProductName": item.PRODUCTID.Product_Name if item.PRODUCTID else None,
                            "Quantity": item.Quantity,
                            "Price": item.Price,
                            "OfferTitle": item.OFFERID.Offer_Title if item.OFFERID else None,
                        }
                        for item in order_items
                    ]
                }
                order_history.append(order_data)

            return Response({"order_history": order_history}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


from decimal import Decimal

class WalletTopUpView(APIView):
    """
    Handles wallet top-up using user_id from the URL.
    """

    def post(self, request, user_id):
        try:
            # Check if wallet exists for the user
            wallet = Wallet.objects.filter(USERID=user_id).first()
            if not wallet:
                return Response(
                    {"error": "Wallet not found for the given user."},
                    status=status.HTTP_404_NOT_FOUND
                )

            # Validate the amount
            amount = request.data.get('amount')
            if not amount:
                return Response(
                    {"error": "Amount is required."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            try:
                # Convert the amount to Decimal
                amount = Decimal(amount)
                if amount <= 0:
                    return Response(
                        {"error": "Amount must be greater than zero."},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            except (ValueError, TypeError, decimal.InvalidOperation):
                return Response(
                    {"error": "Invalid amount format."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Update the wallet balance
            wallet.balance += amount
            wallet.save()

            return Response(
                {
                    "message": "Wallet topped up successfully.",
                    "balance": wallet.balance,
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": f"An unexpected error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



from django.contrib.auth.models import User

class AddReviewAPIView(APIView):
    def post(self, request):
        try:
            product_id = request.data.get('product_id')
            print(f"Product ID: {product_id}")  #
            username = request.data.get('username')
            print(username)
            rating = request.data.get('rating')
            print(rating)
            comment = request.data.get('comment')
            print(comment)

            # Validate product and user existence
            try:
                product = Product_Table.objects.get(id=product_id)
                print(product)
            except Product_Table.DoesNotExist:
                return Response({"success": False, "message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

            try:
                user = User_Table.objects.get(id=username)  # Assuming LOGINID is used to identify users
                print(f"Found user with ID: {user.id}")
            except User.DoesNotExist:
                return Response({"success": False, "message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

            # Save the review
            review = Rating_Review_Table.objects.create(
                USERLID=user,        # Correct field name 'USERLID'
                PRODUCTID=product,   # Correct field name 'PRODUCTID'
                Rating=rating,       # Correct field name 'Rating'
                Review=comment, 
                Date=date.today() 
            )
            serializer = ReviewSerializerview(review)
            return Response({"success": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"success": False, "message": f"Error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ViewProductReviewsAPIView(APIView):
    def get(self, request, product_id):
        try:
            # Fetch reviews with related user details
            reviews = Rating_Review_Table.objects.filter(PRODUCTID=product_id, is_active=True).select_related('USERLID')

            # Serialize the reviews
            serializer = ReviewSerializerview(reviews, many=True)
            
            return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)
        
        except Rating_Review_Table.DoesNotExist:
            return Response({"success": False, "message": "No reviews found for this product."}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response({"success": False, "message": f"Error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DeleteReviewAPIView(APIView):
    def delete(self, request, review_id):
        try:
            review = Rating_Review_Table.objects.get(id=review_id)
            review.delete()
            return Response({"success": True, "message": "Review deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Rating_Review_Table.DoesNotExist:
            return Response({"success": False, "message": "Review not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"success": False, "message": f"Error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        

