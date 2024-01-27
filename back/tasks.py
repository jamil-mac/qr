# from celery import shared_task
# from django.utils import timezone
# from .models import EventModel, UserModel
#
# @shared_task
# def delete_expired_data():
#     current_time = timezone.now()
#
#     expired_events = EventModel.objects.filter(date__lt=current_time.date())
#     expired_events.delete()
#
#     expired_users = UserModel.objects.filter(event__date__lt=current_time.date())
#     for user in expired_users:
#         if user.qr_code:
#             user.qr_code.delete()
#
#     expired_users.delete()