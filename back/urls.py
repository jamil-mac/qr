from django.urls import path

from back.views import EventsListView, EventDetailView, UserCreateView, EventCreateView, UserQRCodeView, export_data, \
    web_hook_view

app_name = 'back'

urlpatterns = [
    path('', EventsListView.as_view(), name='events'),
    path('<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('event/create/', EventCreateView.as_view(), name='event-create'),
    path('register/', UserCreateView.as_view(), name='user-create'),
    path('user/<int:pk>/', UserQRCodeView.as_view(), name='user-detail'),

    path('export/<int:pk>/', export_data, name='export-excel'),
    path('webhook/', web_hook_view, name='webhook'),

]
