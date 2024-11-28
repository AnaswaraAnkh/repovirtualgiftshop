

from django.urls import path

from Admin.views import Accept_Shop, Adminhomepage, OrderAccept, OrderReject, Reject_Shop, Reply, UpdateOrderStatus, Verify_Shop, ViewComplaint



urlpatterns = [
    
   path('Adminhome/',Adminhomepage.as_view(),name='Adminhome'),
   path('Verify_Shop',Verify_Shop.as_view(),name='Verify_Shop'),
   path('accept_shop/<int:shop_id>/', Accept_Shop.as_view(), name='accept_shop'),
   path('reject_shop/<int:shop_id>/', Reject_Shop.as_view(), name='reject_shop'),
   path('ViewComplaint',ViewComplaint.as_view(),name='ViewComplaint'),
   path('Reply/<int:C_id>/',Reply.as_view(),name='Reply'),
   path('updateorderstatus',UpdateOrderStatus.as_view(),name="UpdateOrderStatus"),
   path('AcceptOrder/<int:id>/',OrderAccept.as_view(),name='OrderAccept'),
   path('OrderReject/<int:id>/',OrderReject.as_view(),name='OrderReject'),

   
   ]
