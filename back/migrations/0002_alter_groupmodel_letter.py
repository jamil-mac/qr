# Generated by Django 3.2.12 on 2024-01-27 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmodel',
            name='letter',
            field=models.CharField(blank=True, max_length=3, null=True, verbose_name='letter'),
        ),
    ]
