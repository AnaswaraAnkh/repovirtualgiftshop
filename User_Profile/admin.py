from django.contrib import admin

from User_Profile.models import Chatbot_Table, Delivery_Table, User_Table, Wallet

# Register your models here.
admin.site.register(User_Table)
admin.site.register(Delivery_Table)
admin.site.register(Chatbot_Table)
admin.site.register(Wallet)
