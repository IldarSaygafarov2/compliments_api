# Generated by Django 5.1 on 2024-08-29 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_compliment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compliment',
            name='send_to',
        ),
    ]
