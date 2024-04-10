from rest_framework import serializers
from .models import SentMessage

class SentMessageSerializer(serializers.ModelSerializer):
    """Serializer for unique announcement message sent."""
    class Meta:
        model = SentMessage
        fields = ['unique_id', 'message', 'sent_at']