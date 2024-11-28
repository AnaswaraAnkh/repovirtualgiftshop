from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
import re, math
from collections import Counter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection
from rest_framework.views import APIView

from User_Profile.models import User_Table
from chatbot.models import ChatHistory, KnowledgeBase
from chatbot.serializer import ChatHistorySerializer
from rest_framework import status



# from chatbot.models import Dataset

# @api_view(['POST'])
# def chatbot_response(request):
#     question = request.data.get('question', '')

#     if not question:
#         return JsonResponse({"answer": "Please provide a question."})

#     # Preprocess question
#     question = question.lower().strip()  # Standardize input

#     # Fetch all questions from the database
#     questions = Dataset.objects.filter(is_active=True).values_list('question', flat=True)

#     def text_to_vector(text):
#         words = re.findall(r'\w+', text)
#         return Counter(words)

#     def get_cosine(vec1, vec2):
#         intersection = set(vec1.keys()) & set(vec2.keys())
#         numerator = sum([vec1[x] * vec2[x] for x in intersection])
#         sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
#         sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
#         denominator = math.sqrt(sum1) * math.sqrt(sum2)

#         if not denominator:
#             return 0.0
#         else:
#             return float(numerator) / denominator

#     vector1 = text_to_vector(question)

#     # Store cosine similarity results
#     res = []
#     for db_question in questions:
#         vector2 = text_to_vector(db_question.lower().strip())
#         cosine = get_cosine(vector1, vector2)
#         res.append(cosine)

#     # Find the best match
#     best_match_index = res.index(max(res)) if res else -1
#     best_match_score = max(res) if res else 0

#     # Fetch the corresponding answer
#     if best_match_score > 0.3:  # Adjust this threshold as needed
#         answer = Dataset.objects.filter(question=questions[best_match_index]).values_list('answer', flat=True).first()
#         return JsonResponse({"answer": answer})
#     else:
#         return JsonResponse({"answer": "I cannot understand the question."})


class ChatHistoryAPIView(APIView):
    
    def get(self, request, user_id):
        try:
            user = User_Table.objects.get(id=user_id)  # Fetch the user by ID
            chats = ChatHistory.objects.filter(user=user).order_by("timestamp")
            serializer = ChatHistorySerializer(chats, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except user.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, user_id=None):
        if user_id:
            try:
                user = User_Table.objects.get(id=user_id)
            except User_Table.DoesNotExist:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

            user_message = request.data.get("question","")
            
            # Save user's message
            ChatHistory.objects.create(user=user, message=user_message, sender="user")
            
            # Check if the question exists in the knowledge base
            try:
                kb_entry = KnowledgeBase.objects.get(question__iexact=user_message)
                bot_response = kb_entry.answer
            except KnowledgeBase.DoesNotExist:
                bot_response = "I'm sorry, I don't have an answer to that question."
            
            # Save bot's response
            ChatHistory.objects.create(user=user, message=bot_response, sender="bot")
            
            return Response(
                {"user_message": user_message, "bot_response": bot_response},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response({"error": "user_id is required"}, status=status.HTTP_400_BAD_REQUEST)