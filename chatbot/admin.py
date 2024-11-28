from django.contrib import admin

from chatbot.models import ChatHistory, KnowledgeBase

# Register your models here.
admin.site.register(ChatHistory)
admin.site.register(KnowledgeBase)