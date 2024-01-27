from django.urls import path

from back.views import EventsListView, EventDetailView, UserCreateView, EventCreateView

app_name = 'back'

urlpatterns = [
    path('', EventsListView.as_view(), name='events'),
    path('<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('event/create/', EventCreateView.as_view(), name='event-create'),
    path('register/', UserCreateView.as_view(), name='user-create')
]
