import os
from io import BytesIO
import qrcode
from django.core.files.base import ContentFile
from django.db import models


class EventModel(models.Model):
    event_name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.event_name} in {self.date} at {self.time}'

    class Meta:
        verbose_name = 'event'
        verbose_name_plural = 'events'


class FacultyModel(models.Model):
    faculty_name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.faculty_name

    class Meta:
        verbose_name = 'faculty'
        verbose_name_plural = 'faculties'


class UserModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    event = models.ForeignKey(
        EventModel,
        on_delete=models.CASCADE,
        related_name='users',
    )
    faculty = models.ForeignKey(
        FacultyModel,
        on_delete=models.CASCADE,
        related_name='users',
    )
    group = models.CharField(max_length=5)
    qr_code = models.ImageField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

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
        verbose_name = 'user'
        verbose_name_plural = 'users'


class AnotherUserModel(models.Model):
    academic_degree = models.CharField(max_length=30, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    event = models.ForeignKey(
        EventModel,
        on_delete=models.CASCADE,
        related_name='another_users',
    )

    qr_code = models.ImageField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

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
        verbose_name = 'another user'
        verbose_name_plural = 'another users'
