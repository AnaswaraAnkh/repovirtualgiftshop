from django.db import models

from User_Profile.models import User_Table

# Create your models here.
class ChatHistory(models.Model):
    user = models.ForeignKey(User_Table, on_delete=models.CASCADE, related_name="chats")
    message = models.TextField()
    sender = models.CharField(max_length=10, choices=[("user", "User"), ("bot", "Bot")])
    timestamp = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.user.username} - {self.message[:30]}"

# Knowledge Base model
class KnowledgeBase(models.Model):
    question = models.TextField(unique=True)
    answer = models.TextField()

    def _str_(self):
        return self.question[:50]