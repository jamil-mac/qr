import logging
import os

from celery import shared_task
from django.db import transaction
from django.utils import timezone
from openpyxl.workbook import Workbook

from qr import settings
from .models import EventModel, UserModel, FacultyModel
from .views import send_excel_file

logger = logging.getLogger(__name__)


@shared_task
def delete_expired_data():
    try:
        with transaction.atomic():
            current_time = timezone.now()

            expired_events = EventModel.objects.filter(date__lt=current_time.date())


            if expired_events.count() != 0:
                for expired_event in expired_events:
                    wb = Workbook()
                    sheet = wb.active
                    users = expired_event.users.all()
                    faculties = FacultyModel.objects.all()

                    faculty_counts = {faculty.faculty_name: 0 for faculty in faculties}

                    for user in users:
                        faculty_name = user.faculty.faculty_name
                        faculty_counts[faculty_name] += 1

                    for faculty_name, count in faculty_counts.items():
                        sheet.append([faculty_name, count])

                    filename = expired_event.event_name

                    send_excel_file(wb, filename)
                    expired_event.delete()
                    wb.remove(sheet)

            expired_users = UserModel.objects.filter(event__date__lt=current_time.date())
            for user in expired_users:
                print('first ' + user.qr_code)
                print(str(user.qr_code))
                if user.qr_code:
                    delete_media_file(f'qrcodes/{str(user.qr_code)}')

                print(str(user.qr_code))

            expired_users.delete()
    except Exception as e:
        logger.error(f"Error deleting user: {e}")


def delete_media_file(file_path):
    try:
        absolute_path = os.path.join(settings.MEDIA_ROOT, file_path)

        if os.path.exists(absolute_path):
            os.remove(absolute_path)
            print(f"File {file_path} deleted successfully.")
        else:
            print(f"File {file_path} does not exist.")
    except Exception as e:
        print(f"Error deleting file {file_path}: {e}")
