from django.contrib import admin

from Shop.models import *

# Register your models here.
admin.site.register(Shop_Table)
admin.site.register(Product_Table)
admin.site.register(Offer_Table)
admin.site.register(Order_Table)
admin.site.register(Orderitem_Table)
admin.site.register(Complaint_Table)
admin.site.register(Rating_Review_Table)
admin.site.register(Category)
