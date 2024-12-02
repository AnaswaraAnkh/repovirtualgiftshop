from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from Login.models import LoginTable
from Shop.models import Complaint_Table, Order_Table, Shop_Table
from Admin.forms import Complaint_replyForm



# Create your views here.
class Adminhomepage(View):
    def get(self,request):
        return render(request,"Adminhomepage.html")
    
class Verify_Shop(View):
    def get(self,request):
        obj = Shop_Table.objects.all()
        # obj=Shop_Table.objects.filter(LOGINID__user_type='Pending')
        print(obj)
        return render(request,'Verify Shop.html',{'val':obj})
    
class Accept_Shop(View):
    def get(self, request, shop_id):
        try:
            shop = Shop_Table.objects.get(id=shop_id)  # Fetch the instance
            shop.LOGINID.user_type = 'Shop'  # Update the status
            shop.LOGINID.save()  # Save the changes
            return HttpResponse('''<script>alert("successfully Accepted");window.location="/giftadmin/Verify_Shop"</script>''')  
        except LoginTable.DoesNotExist:
            # Handle the case where the shop doesn't exist
            return HttpResponse("Shop not found", status=404)
        
class Reject_Shop(View):
    def get(self, request, shop_id):
        try:
            shop = Shop_Table.objects.get(id=shop_id)  # Fetch the instance
            shop.LOGINID.user_type = 'Rejected'  # Update the status
            shop.LOGINID.save()  # Save the changes
            return HttpResponse('''<script>alert("successfully Rejected");window.location="/giftadmin/Verify_Shop"</script>''')  
        except LoginTable.DoesNotExist:
            # Handle the case where the shop doesn't exist
            return HttpResponse("Shop not found", status=404)
        

class ViewComplaint(View):
    def get(self,request):
        obj=Complaint_Table.objects.select_related('USERLID').all()
        return render(request,'View Complaints.html',{'val':obj})
    
class Reply(View):
    def get(self,request,C_id):
        obj=Complaint_Table.objects.get(id=C_id)
        print(obj)
        return render(request,"Reply.html",{'val':obj})
    def post(self, request, C_id):
        obj = Complaint_Table.objects.get(id=C_id)
        form = Complaint_replyForm(request.POST, instance=obj)

        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("Successfully Replied");window.location="/giftadmin/ViewComplaint"</script>''')
        else:
            # Print form errors for debugging
            print(form.errors)
            return HttpResponse('''<script>alert("Failed to reply. Please check form errors.");window.location="/giftadmin/ViewComplaint"</script>''')
        

class UpdateOrderStatus(View):
    def get(self,request):
        obj=Order_Table.objects.filter(Order_Status="Pending")
        print(obj)
        return render(request,"orderupdatestatus.html",{'val':obj})
    
class OrderAccept(View):
    def get(self, request,id):
            order = Order_Table.objects.get(id=id)  # Fetch the instance
            order.Order_Status = 'Completed'  # Update the status
            order.save()  # Save the changes
            return HttpResponse('''<script>alert("successfully Accepted");window.location="/giftadmin/updateorderstatus"</script>''')  
    
class OrderReject(View):
    def get(self, request,id):
            order = Order_Table.objects.get(id=id)  # Fetch the instance
            order.Order_Status = 'Rejected'  # Update the status
            order.save()  # Save the changes
            return HttpResponse('''<script>alert("successfully Rejected");window.location="/giftadmin/updateorderstatus"</script>''') 
        



# class Shopvieworder()
        