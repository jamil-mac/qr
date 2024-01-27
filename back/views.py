from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from back.forms import UserRegistrationForm, EventCreateForm
from back.models import EventModel, UserModel, FacultyModel, GroupModel


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


class UserCreateView(CreateView):
    model = UserModel
    template_name = 'registration.html'
    form_class = UserRegistrationForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = EventModel.objects.all()
        context['faculties'] = FacultyModel.objects.all()
        context['groups'] = GroupModel.objects.all()
        return context

    def form_valid(self, form):
        return super().form_valid(form)


class EventCreateView(CreateView):
    model = EventModel
    template_name = 'event_create.html'
    form_class = EventCreateForm
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)
