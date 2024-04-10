from celery import shared_task
from django.db import IntegrityError
from .models import SentMessage
import requests
from datetime import datetime


@shared_task
def send_announcement(unique_id, message):
    """
    Cron job task to sent unique announcement message. 
    A check is done to check that no other message with the same id is sent.
    """
    url = reverse('message-list')
   

    try:
        # Send request to API
        message = SentMessage.objects.create(unique_id=unique_id, message=message, sent_at=datetime.now().timestamp())

        message_data = {'messages': message}
        response = requests.post(url, json=message_data)

        print(f"Message sent: {message}")
        if response.status_code == 200:
            print('Message sent successfully')
        else:
            print('Failed to send message to API. Status code: {}'.format(response.status_code))
    except IntegrityError:
        print("Message with this unique ID has already been sent.")