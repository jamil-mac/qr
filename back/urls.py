from django.urls import path

from back.views import EventsListView, EventDetailView, UserCreateView, EventCreateView, UserQRCodeView, export_data, \
    web_hook_view, AnotherUserCreateView, AnotherUserQRCodeView

app_name = 'back'

urlpatterns = [
    # events
    path('events/list/', EventsListView.as_view(), name='events'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('event/create/', EventCreateView.as_view(), name='event-create'),

    # users
    path('', UserCreateView.as_view(), name='user-create'),
    path('another/', AnotherUserCreateView.as_view(), name='another-user-create'),
    path('user/<int:pk>/', UserQRCodeView.as_view(), name='user-detail'),
    path('another/user/<int:pk>/', AnotherUserQRCodeView.as_view(), name='another-user-detail'),

    # webhook and excel
    path('export/<int:pk>/', export_data, name='export-excel'),
    path('webhook/', web_hook_view, name='webhook'),
]
