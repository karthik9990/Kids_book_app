from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    pdf_file = models.FileField(upload_to='pdfs/', blank=True, null=True)

    def __str__(self):
        return self.title


class Page(models.Model):
    book = models.ForeignKey(Book, related_name='pages', on_delete=models.CASCADE)
    page_number = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return f"{self.book.title} - Page {self.page_number}"
