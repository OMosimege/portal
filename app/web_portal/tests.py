from django.test import TestCase
from django.utils import timezone
from unittest.mock import patch
from web_portal.models import SentMessage
from web_portal.tasks import send_announcement

class SendAnnouncementTestCase(TestCase):
    def setUp(self):
        self.existing_message = SentMessage.objects.create(
            message="This is a test message.",
            sent_at=timezone.now()
        )
        print("message")
        print(self.existing_message)

    @patch('web_portal.tasks.send_announcement') 
    def test_sends_message_once(self, mock_send_message):
        print("cron job send first")
        send_announcement()

        mock_send_message.assert_called_once()

    @patch('web_portal.tasks.send_announcement')  
    def test_does_not_send_message_if_already_sent(self, mock_send_message):
        self.existing_message.sent_at = timezone.now()
        self.existing_message.save()

        print("cron job send second")
        send_announcement()

        mock_send_message.assert_not_called()

