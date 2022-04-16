from django.contrib import admin
from django.urls import register_converter

from books.converters import PubDateConverter
from books.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'pub_date',)


admin.site.register(Book, BookAdmin)
register_converter(PubDateConverter, 'date')
