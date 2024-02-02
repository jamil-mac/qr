import logging
import os

from celery import shared_task
from django.utils import timezone

from qr import settings
from .models import EventModel, UserModel

logger = logging.getLogger(__name__)


@shared_task
def delete_expired_data():
    try:
        current_time = timezone.now()

        expired_events = EventModel.objects.filter(date__lt=current_time.date())
        expired_events.delete()

        expired_users = UserModel.objects.filter(event__date__lt=current_time.date())
        for user in expired_users:
            print('first ' + user.qr_code)
            if user.qr_code:
                delete_media_file(f'qrcodes/{str(user.qr_code)}')

            print(str(user.qr_code))

        expired_users.delete()
    except Exception as e:
        logger.error(f"Error deleting user: {e}")


def delete_media_file(file_path):
    # absolute_path = os.path.join(settings.MEDIA_ROOT, file_path)
    #
    # if os.path.exists(absolute_path):
    #     os.remove(absolute_path)
    #     print(f"File {file_path} deleted successfully.")
    # else:
    #     print(f"File {file_path} does not exist.")
    try:
        absolute_path = os.path.join(settings.MEDIA_ROOT, file_path)

        if os.path.exists(absolute_path):
            os.remove(absolute_path)
            print(f"File {file_path} deleted successfully.")
        else:
            print(f"File {file_path} does not exist.")
    except Exception as e:
        print(f"Error deleting file {file_path}: {e}")
