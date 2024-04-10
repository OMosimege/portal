from django.shortcuts import render
import requests
from rest_framework import viewsets
from .models import SentMessage
from .serializers import SentMessageSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = SentMessage.objects.all()
    serializer_class = SentMessageSerializer




def message_list(request):
    response = requests.get('http://localhost:8000/api/messages/')
    messages = response.json()
    return render(request, 'web_portal/message_list.html', {'messages': messages})
