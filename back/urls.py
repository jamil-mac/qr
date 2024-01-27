from django.urls import path

from back.views import EventsListView, EventDetailView

app_name = 'back'

urlpatterns = [
    path('', EventsListView.as_view(), name='events'),
    path('<int:pk>/', EventDetailView.as_view(), name='event-detail'),
]
