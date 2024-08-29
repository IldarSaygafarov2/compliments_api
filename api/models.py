from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    chat_id = models.BigIntegerField(unique=True, null=True)


class ComplimentTypeChoices(models.TextChoices):
    SIMPLE = 'simple', 'Обычный'
    SPECIAL = 'special', 'Специальный'
    EXTRA_SPECIAL = 'extra_special', 'Интимный'


class Compliment(models.Model):
    text = models.TextField()
    compliment_type = models.CharField(max_length=15, choices=ComplimentTypeChoices.choices,
                                       default=ComplimentTypeChoices.SIMPLE,)



