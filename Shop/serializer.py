from rest_framework.serializers import ModelSerializer

from User_Profile.models import User_Table
from Login.models import LoginTable
from Shop.models import Complaint_Table


from rest_framework import serializers
from .models import Complaint_Table

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint_Table
        fields = ['USERLID','Complaint','Reply']



      
    
