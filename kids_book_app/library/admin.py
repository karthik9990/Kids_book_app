from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pdf_file')


admin.site.register(Book)
