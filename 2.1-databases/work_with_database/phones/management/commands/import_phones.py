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
            if request.method == 'POST':
                form = PhoneImportForm(request.POST, request.FILES)
                if form.is_valid():
                    form_object = form.save()
                    with form_object.csv_file.open('r') as csv_file:
                        rows = csv.reader(csv_file, delimiter=';')
                        if next(rows) != ['name', 'author', 'publish_date']:
                            messages.warning(request, 'Неверные заголовки у файла')
                            return HttpResponseRedirect(request.path_info)
                        for row in rows:
                            print(row[2])
                            Phone.objects.update_or_create(
                                name=row[0],
                                author=row[1],
                                publish_date=row[2]
                            )
                    url = reverse('admin:index')
                    messages.success(request, 'Файл успешно импортирован')
                    return HttpResponseRedirect(url)
            form = PhoneImportForm()
            return render(request, 'admin/csv_import_page.html', {'form': form})