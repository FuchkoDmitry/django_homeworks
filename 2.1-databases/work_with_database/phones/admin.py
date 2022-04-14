from django.contrib import admin
from phones.models import Phone
# Register your models here.


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'release_date']
    list_filter = ['price', 'release_date', 'name', 'lte_exists']
    # вариант 2
    # prepopulated_fields = {'slug': ('name', )}
