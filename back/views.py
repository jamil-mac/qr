from django.shortcuts import render
from django.views.generic import ListView, DetailView

from back.models import EventModel


class EventsListView(ListView):
    template_name = 'events.html'
    queryset = EventModel.objects.order_by('-pk')
    context_object_name = 'events'


class EventDetailView(DetailView):
    template_name = 'event_detail.html'
    model = EventModel

    def get_context_data(self, *args, **kwargs):
        context = super(EventDetailView, self).get_context_data(*args, **kwargs)
        event_instance = self.get_object()
        context['users'] = event_instance.users.all()
        return context

