from django.db import models



class SentMessage(models.Model):
    """Model with unique ID for each announcement message sent"""
    unique_id = models.CharField(max_length=255, unique=True)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)