from rest_framework.serializers import ModelSerializer

from chatbot.models import ChatHistory, KnowledgeBase


class ChatHistorySerializer(ModelSerializer):
    class Meta:
        model = ChatHistory
        fields = ['id', 'user', 'message', 'sender', 'timestamp']
        read_only_fields = ['timestamp']

# Knowledge Base Serializer
class KnowledgeBaseSerializer(ModelSerializer):
    class Meta:
        model = KnowledgeBase
        fields = ['id', 'question','answer']