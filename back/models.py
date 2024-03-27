import os
from io import BytesIO
import qrcode
from django.core.files.base import ContentFile
from django.db import models
from django.utils.translation import gettext_lazy as _


class EventModel(models.Model):
    event_name = models.CharField(max_length=255, verbose_name=_('event_name'))
    date = models.DateField(verbose_name=_('date'))
    time = models.TimeField(verbose_name=_('time'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return f'{self.event_name} in {self.date} at {self.time}'

    class Meta:
        verbose_name = _('event')
        verbose_name_plural = _('events')


class FacultyModel(models.Model):
    faculty_name = models.CharField(max_length=255, verbose_name=_('faculty_name'))
    abbreviation = models.CharField(max_length=100, verbose_name=_('abbreviation'), null=True, blank=True)

    def __str__(self):
        return self.faculty_name

    class Meta:
        verbose_name = _('faculty')
        verbose_name_plural = _('faculties')


class GroupModel(models.Model):
    group_number = models.IntegerField(verbose_name=_('group_number'))
    letter = models.CharField(max_length=3, verbose_name=_('letter'), null=True, blank=True)

    def get_name(self):
        return f'{self.group_number}-{self.letter}' if self.letter is not None else f'{self.group_number}'

    def __str__(self):
        return f'{self.group_number}-{self.letter}' if self.letter is not None else f'{self.group_number}'

    class Meta:
        verbose_name = _('group')
        verbose_name_plural = _('groups')


class UserModel(models.Model):
    first_name = models.CharField(max_length=100, verbose_name=_('first_name'))
    last_name = models.CharField(max_length=100, verbose_name=_('last_name'))
    phone_number = models.CharField(max_length=13, verbose_name=_('phone_number'))
    event = models.ForeignKey(
        EventModel,
        on_delete=models.CASCADE,
        related_name='users',
        verbose_name=_('event')
    )
    faculty = models.ForeignKey(
        FacultyModel,
        on_delete=models.CASCADE,
        related_name='users',
        verbose_name=_('faculty')
    )
    group = models.ForeignKey(
        GroupModel,
        on_delete=models.CASCADE,
        related_name='users',
        verbose_name=_('group')
    )
    qr_code = models.ImageField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def save(self, *args, **kwargs):
        if not self.qr_code:
            self.generate_qr_code()
        super().save(*args, **kwargs)

    def generate_qr_code(self):
        data = f"{self.event.event_name} - {self.first_name} - {self.last_name}"
        qr = qrcode.QRCode(
            version=3,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        directory = 'qrcodes/'
        os.makedirs(directory, exist_ok=True)

        img_path = f'{directory}{self.event.event_name}_{self.first_name}_{self.last_name}.png'

        img_bytes_io = BytesIO()
        img.save(img_bytes_io)
        img_bytes_io.seek(0)

        # Save the BytesIO object as the content of the ImageField
        self.qr_code.save(img_path, ContentFile(img_bytes_io.read()), save=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name} registered to {self.event.event_name}'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


class AnotherUserModel(models.Model):
    academic_degree = models.CharField(max_length=30, verbose_name=_('academic_degree'), null=True, blank=True)
    first_name = models.CharField(max_length=100, verbose_name=_('first_name'))
    last_name = models.CharField(max_length=100, verbose_name=_('last_name'))
    phone_number = models.CharField(max_length=13, verbose_name=_('phone_number'))
    event = models.ForeignKey(
        EventModel,
        on_delete=models.CASCADE,
        related_name='another_users',
        verbose_name=_('event')
    )

    qr_code = models.ImageField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def save(self, *args, **kwargs):
        if not self.qr_code:
            self.generate_qr_code()
        super().save(*args, **kwargs)

    def generate_qr_code(self):
        data = f"{self.event.event_name} - {self.first_name} - {self.last_name}"
        qr = qrcode.QRCode(
            version=3,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        directory = 'qrcodes/'
        os.makedirs(directory, exist_ok=True)

        img_path = f'{directory}{self.event.event_name}_{self.first_name}_{self.last_name}.png'

        img_bytes_io = BytesIO()
        img.save(img_bytes_io)
        img_bytes_io.seek(0)

        self.qr_code.save(img_path, ContentFile(img_bytes_io.read()), save=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name} registered to {self.event.event_name}'

    class Meta:
        verbose_name = _('another user')
        verbose_name_plural = _('another users')
