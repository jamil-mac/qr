# Generated by Django 4.2.9 on 2024-01-26 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0002_usermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='qr',
            field=models.ImageField(upload_to='qrcodes/'),
        ),
    ]
