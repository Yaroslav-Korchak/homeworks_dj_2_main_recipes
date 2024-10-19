import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from phones.models import Phone

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            try:
                price = int(phone['price'])
            except ValueError:
                price = None  # Или значение по умолчанию, если есть ошибка

            try:
                release_date = datetime.strptime(phone['release_date'], '%Y-%m-%d').date()
            except ValueError:
                release_date = None

            Phone.objects.create(
                id=phone['id'],
                name=phone['name'],
                price=price,
                image=phone['image'],
                release_date=release_date,
                lte_exists=phone['lte_exists'] == 'True',
                slug=slugify(phone['name'])
            )
