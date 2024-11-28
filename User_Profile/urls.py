

from django.urls import path

from User_Profile.views import   AddReviewAPIView, CategoryListView, DeleteReviewAPIView, LoginPage, OrderHistoryView, PlaceOrderView,UpdateProfileImage, UserReg ,UserProfileView,ProductWithOffersView1, ViewProductReviewsAPIView,WalletBalanceAPIView, WalletTopUpView

urlpatterns = [

    path('register', UserReg.as_view(), name='user_register'),
     path('loginapi/',LoginPage.as_view(),name="Loginpage"),
    #viewprofile
    path('profile/<int:id>', UserProfileView.as_view(), name='user-profile'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    
    path('productswithoffers/', ProductWithOffersView1.as_view(), name='product-with-offers1'),
    path('walletview/<int:id>/', WalletBalanceAPIView.as_view(), name='wallet-balance'),
    path('update-profile-image/<int:id>/', UpdateProfileImage.as_view(), name='update-profile-image'),
    path('place-order/<int:user_id>/', PlaceOrderView.as_view(), name='place-order'),
    path('history/<int:user_id>/', OrderHistoryView.as_view(), name='order_history'),
    path('topup/<int:user_id>/', WalletTopUpView.as_view(), name='topup-wallet'),
    path('reviews', AddReviewAPIView.as_view(), name='add-review'),
    path('reviews/<int:product_id>/', ViewProductReviewsAPIView.as_view(), name='view-reviews'),
    path('reviews/<int:review_id>/delete/', DeleteReviewAPIView.as_view(), name='delete-review'),
     
]
