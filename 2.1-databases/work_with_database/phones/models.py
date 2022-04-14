from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40, verbose_name='Модель')
    price = models.IntegerField(null=False, verbose_name='Цена')
    image = models.CharField(max_length=100, null=False)
    release_date = models.DateField(null=False, verbose_name='Дата выпуска')
    lte_exists = models.BooleanField(null=False)
    slug = models.SlugField(max_length=50, unique=True, verbose_name='URL')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)
