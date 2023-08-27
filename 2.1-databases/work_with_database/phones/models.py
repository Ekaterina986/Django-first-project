from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='name')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)

# class PhoneImport(models.Model):
#     csv_file = models.FileField(upload_to='uploads/')
#     date_added = models.DateTimeField(auto_now_add=True)
