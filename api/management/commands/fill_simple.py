from django.core.management.base import BaseCommand
import json
from api.models import Compliment


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('compliments.json', 'r', encoding='utf-8') as f:
            compliments = json.load(f)

            for compliment in compliments:
                obj = Compliment(text=compliment[0])
                obj.save()
                print('добавлено')
