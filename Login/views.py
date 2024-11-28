import json
from django.http import JsonResponse
from django.views import View
from django.shortcuts import redirect, render

from Login.models import LoginTable, Token
from django.contrib import messages

from django.contrib.auth import authenticate

from Shop.models import Shop_Table
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

class Login_view(View):
    def get(self, request):
        return render(request, 'Login.html')
    def post(self, request):
        user_type = ""
        response_dict = {"success": False}
        landing_page_url = {
            "Admin": "Adminhome",
            "Shop":"shophomepage"



        }
        username = request.POST.get("username")
        print(username, 'username')
        password = request.POST.get("password")
        print(password, 'password')

        try:

            user = LoginTable.objects.get(username=username)
        except LoginTable.DoesNotExist:
            response_dict[
                "reason"
            ] = "no account found for this user name,please sign up."
            messages.error(request, response_dict["reason"])
            print(response_dict["reason"])
            return render(request,'login.html', {"error_message": response_dict.get("reason", "")})

        user = LoginTable.objects.filter(username=username, is_active="False").first()
        # print("is_activestatus",user.is_active)
        if user:
            response_dict[
                "reason"
            ] = "user is inactive ,pls contact admin."
            messages.error(request, response_dict["reason"])
            print(response_dict["reason"])
            return render(request,'login.html', {"error_message": response_dict.get("reason", "")})
        # authenticated = authenticate(email=username, password=password)
        # try:
        # print("invalid credentials")
        # user = Userprofile.objects.filter(email=username,is_active=True,password=password).first()
        # if user:
        #     response_dict[
        #         "reason"
        #     ]="invalid credentials."
        #     messages.error(request,response_dict["reason"])
        #     return render(request, self.templates_name, {"error_message": response_dict.get("reason", "")})
        user = authenticate(username=username, password=password)

        # user = Userprofile.objects.filter(email=username, is_active="True",password=password).first()
        print(user, 'auth')
        if user:
            session_dict = {"real_user": user.id}
            token, c = Token.objects.get_or_create(
                user=user, defaults={"session_dict": json.dumps(session_dict)}
            )

            user_type = user.user_type
            request.session["data"] = {
                "user_id": user.id,
                "user_type": user.user_type,
                "token": token.key,
                "username": user.username,
                "status": user.is_active,
            }
            print(user)
            print(user_type)
            request.session["user_id"] = user.id
            request.session["user"] = user.username
            request.session["token"] = token.key
            request.session["status"] = user.is_active
            return redirect(landing_page_url[user_type])
        else:
            response_dict[
                "reason"
            ] = "invalid credentials."
            messages.error(request, response_dict["reason"])
            print(response_dict["reason"])
            return render(request,'login.html', {"error_message": response_dict.get("reason", "")})
        return render(request,'Homepage.html', {"error_message": response_dict.get("reason","")})

class Sendotp(View):
    def get(self, request):
        # Render the forget password form
        return render(request, 'forgetpassword.html')
    
    def post(self, request):
        # Get the email from the form data
        email = request.POST.get('email')
        print('email:', email)
        
        try:
            # Query the LoginTable for a record matching the given email
            clientinstance = LoginTable.objects.filter(username=email).first()
            print('clientinstance:', clientinstance)
            
            # If no such user exists, raise an exception
            if not clientinstance:
                raise LoginTable.DoesNotExist
        except LoginTable.DoesNotExist:
            # Return a JSON response indicating the user was not found
            return JsonResponse({'message': 'User not found.'}, status=404)
        
        # Generate a 6-digit OTP
        otp = get_random_string(length=6, allowed_chars='0123456789')
        hashed_otp = make_password(otp)  # Hash the OTP if you prefer storing it securely
        print('Generated OTP:', otp)

        # Save the hashed OTP to the client instance in the OTP field
        clientinstance.otp = hashed_otp  # If you want to store the hashed OTP
        clientinstance.save()

        # Send the OTP via email
        send_mail(
            'Forgot Password OTP',
            f'Your one-time password (OTP) is: {otp}',
            'anaswaraankh@gmail.com',  # Change to your email
            [email],
            fail_silently=False,
        )

        return JsonResponse({'message': 'OTP sent successfully. Check your email.'}, status=200)
    

