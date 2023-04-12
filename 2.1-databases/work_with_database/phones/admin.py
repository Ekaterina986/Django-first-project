from django.contrib import admin
from .models import Phone, PhoneImport
import csv
from .forms import PhoneImportForm
from django.urls import path
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages


# Register your models here.

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'image', 'release_date', 'lte_exists', 'slug',)

    def get_urls(self):
        urls = super().get_urls()
        urls.insert(-1, path('csv-upload/', self.upload_csv))
        return urls

    def upload_csv(self, request):
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


@admin.register(PhoneImport)
class PhoneImportAdmin(admin.ModelAdmin):
    list_import = ('csv_file', 'date_add',)
