# Generated by Django 5.1 on 2024-08-29 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_compliment_send_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='chat_id',
            field=models.BigIntegerField(null=True, unique=True),
        ),
    ]
