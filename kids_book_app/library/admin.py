from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pdf_file')


admin.site.register(Book)
admin.site.site_header = "My Kids Book App Administration"  # This changes the header
admin.site.site_title = "My Kids Book App Admin"            # This changes the title on the browser tab
admin.site.index_title = "Welcome to My Kids Book App Admin"  # This changes the index title
