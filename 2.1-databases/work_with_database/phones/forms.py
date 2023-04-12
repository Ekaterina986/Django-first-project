from django.forms import ModelForm
from .models import PhoneImport

class PhoneImportForm(ModelForm):
    class Meta:
        model = PhoneImport
        fields = ('csv_file',)