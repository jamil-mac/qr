# Generated by Django 3.2.12 on 2024-04-04 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0012_auto_20240328_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anotherusermodel',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]