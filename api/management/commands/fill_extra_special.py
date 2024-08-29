from django.core.management.base import BaseCommand

from api.models import Compliment


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('extra_compliments.txt', mode='r', encoding='utf-8') as f:
            data = f.read().split('==')
            for line in data:
                obj = Compliment(text=line, compliment_type='extra_special')
                obj.save()
                print('special Dobavleno')