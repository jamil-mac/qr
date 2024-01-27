# Generated by Django 3.2.12 on 2024-01-27 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=255, verbose_name='event_name')),
                ('date', models.DateField(verbose_name='date')),
                ('time', models.TimeField(verbose_name='time')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
            },
        ),
        migrations.CreateModel(
            name='FacultyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=255, verbose_name='faculty_name')),
            ],
            options={
                'verbose_name': 'faculty',
                'verbose_name_plural': 'faculties',
            },
        ),
        migrations.CreateModel(
            name='GroupModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_number', models.IntegerField(verbose_name='group_number')),
                ('letter', models.CharField(max_length=3, verbose_name='letter')),
            ],
            options={
                'verbose_name': 'group',
                'verbose_name_plural': 'groups',
            },
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=100, verbose_name='last_name')),
                ('phone_number', models.CharField(max_length=13, verbose_name='phone_number')),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='qrcodes/')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='back.eventmodel', verbose_name='event')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='back.facultymodel', verbose_name='faculty')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='back.groupmodel', verbose_name='group')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
    ]
