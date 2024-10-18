from django.shortcuts import render, get_object_or_404
from .models import Book  # Import the Book model
from django.core.paginator import Paginator


# View for the homepage, showing recent books
def home(request):
    # Get the 10 most recent books
    recent_books = Book.objects.order_by('-id')[:10]
    return render(request, 'library/home.html', {'recent_books': recent_books})


# View for listing all books
def book_list(request):
    books = Book.objects.all()  # Get all books
    paginator = Paginator(book_list, 10)  # Show 10 books per page.
    page_number = request.GET.get('page')
    books = paginator.get_page(page_number)
    return render(request, 'library/book_list.html', {'books': books})


# View for displaying details of a single book
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)  # Get the book object by primary key (id) or return a 404
    return render(request, 'library/book_detail.html', {'book': book})


# Static page for "About Us"
def about_us(request):
    return render(request, 'library/about_us.html')


# Static page for "Contact Us"
def contact_us(request):
    return render(request, 'library/contact_us.html')


def pdf_viewer(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'library/pdf_viewer.html', {'book': book})
