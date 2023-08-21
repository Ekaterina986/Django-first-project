import csv
from audioop import reverse
from pyexpat.errors import messages
from urllib import request

from django.core.management.base import BaseCommand
from django.http import HttpResponseRedirect
from django.shortcuts import render
from phones.models import Phone





class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            print(phone)
            Phone.objects.update_or_create(
                id=phone['id'],
                price=phone['price'],
                name=phone['name'],
                image=phone['image'],
                release_date=phone['release_date'],
                lte_exists=phone['lte_exists'],
                slug=phone['name'],
            )
        return 'ok'