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
        # urls.insert(-1, path('csv-upload/', self.upload_csv))
        return urls



@admin.register(PhoneImport)
class PhoneImportAdmin(admin.ModelAdmin):
    list_import = ('csv_file', 'date_add',)
