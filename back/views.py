from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from back.forms import UserRegistrationForm, EventCreateForm, AnotherUserRegistrationForm
from back.models import EventModel, UserModel, FacultyModel, AnotherUserModel

from django.views.decorators.csrf import csrf_exempt
from openpyxl.workbook import Workbook

import telebot

import io

from django.http import HttpResponse

bot = telebot.TeleBot('6585354812:AAE7RpqTwzYVDaP1rJHDj-ulrlOvtVS_d9c')

URL = 'https://api.telegram.org/bot6585354812:AAE7RpqTwzYVDaP1rJHDj-ulrlOvtVS_d9c'


class EventsListView(ListView):
    template_name = 'events.html'
    queryset = EventModel.objects.order_by('-pk')
    context_object_name = 'events'


class EventDetailView(DetailView):
    template_name = 'event_detail.html'
    model = EventModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event_instance = self.get_object()
        context['users'] = UserModel.objects.filter(event=event_instance)
        context['another_users'] = AnotherUserModel.objects.filter(event=event_instance)
        context['faculties'] = FacultyModel.objects.all()

        context['faculty_counts'] = {faculty.faculty_name: 0 for faculty in context['faculties']}

        for user in context['users']:
            faculty_name = user.faculty.faculty_name
            context['faculty_counts'][faculty_name] += 1

        return context


class UserCreateView(CreateView):
    model = UserModel
    template_name = 'registration.html'
    form_class = UserRegistrationForm

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['events'] = EventModel.objects.all()
        context['faculties'] = FacultyModel.objects.all()
        return context

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        user_pk = self.object.pk
        return reverse('back:user-detail', kwargs={'pk': user_pk})


class AnotherUserCreateView(CreateView):
    model = AnotherUserModel
    template_name = 'another_registration.html'
    form_class = AnotherUserRegistrationForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(AnotherUserCreateView, self).get_context_data(**kwargs)
        context['events'] = EventModel.objects.all()

        return context

    def get_success_url(self):
        user_pk = self.object.pk
        return reverse('back:another-user-detail', kwargs={'pk': user_pk})


class EventCreateView(CreateView):
    model = EventModel
    template_name = 'event_create.html'
    form_class = EventCreateForm
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


class UserQRCodeView(DetailView):
    model = UserModel
    template_name = 'qr_for_user.html'


class AnotherUserQRCodeView(DetailView):
    model = AnotherUserModel
    template_name = 'qr_for_another_user.html'


def export_data(request, pk):
    wb = Workbook()
    sheet = wb.active

    event = EventModel.objects.get(pk=pk)
    users = event.users.all()
    another_users = event.another_users.all()
    faculties = FacultyModel.objects.all()

    faculty_counts = {faculty.faculty_name: 0 for faculty in faculties}

    for user in users:
        faculty_name = user.faculty.faculty_name
        faculty_counts[faculty_name] += 1

    for faculty_name, count in faculty_counts.items():
        sheet.append([faculty_name, count])

    sheet.append(['Erkin tinglovchilar', another_users.count()])

    filename = event.event_name

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename={filename}.xlsx'

    wb.save(response)

    return response


@csrf_exempt
def web_hook_view(request):
    """ setting webhook """
    if request.method == "POST":
        bot.process_new_updates([telebot.types.Update.de_json(request.body.decode('utf-8'))])
        return HttpResponse('ok', status=200)
    return HttpResponse('ok', status=200)


@bot.message_handler(commands=['start'])  # /start
def start(message):
    bot.reply_to(message, "Moto moto")
    print(message.chat.id)


def send_excel_file(wb, filename):
    with io.BytesIO() as output:
        wb.save(output)
        output.seek(0)
        bot.send_document(
            58939309,
            output,
            visible_file_name=filename + '.xlsx'
        )
