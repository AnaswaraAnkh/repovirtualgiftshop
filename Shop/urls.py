

from django.urls import path

from Shop.views import *

urlpatterns = [
    path('shop',shop_registration.as_view(),name='shop_registration'),
    path('shophomepage',Shophomepage.as_view(),name='shophomepage'),
    path('Shop_profile/',Shop_Profile.as_view(),name='Shop_profile'),
    path('ViewProducts',ViewProducts.as_view(),name='ViewProducts'),
    path('AddProducts',AddProducts.as_view(),name='AddProducts'),
    path('ProductEdit/<int:P_id>/',ProductEdit.as_view(),name='ProductEdit'),
    path('ProductDelete/<int:P_id>/',ProductDelete.as_view(),name='ProductDelete'),
    path('ViewOffer',ViewOffer.as_view(),name='ViewOffer'),
    path('AddOffer',AddOffer.as_view(),name='AddOffer'),
    path('OfferEdit/<int:O_id>',OfferEdit.as_view(),name='OfferEdit'),
    path('OfferDelete/<int:O_id>',OfferDelete.as_view(),name='OfferDelete'),
    path('CustomerOrders',CustomerOrders.as_view(),name='CustomerOrders'),
    path('UploadDeliverystatus',UploadDeliverystatus.as_view(),name='UploadDeliverystatus'),
    path('Rating_Review',Rating_Review.as_view(),name='Rating_Review'),
    path('AddCategory',AddCategory.as_view(),name='AddCategory'),
    path('add-complaint/<int:user_id>/', SubmitComplaintView.as_view(), name='submit-complaint'),
    path('get-complaint/<int:user_id>/', FetchComplaintsView.as_view(), name='fetch-complaints'),
   


   
]
