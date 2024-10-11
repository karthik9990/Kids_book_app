from django.urls import path
from . import views  # Import the views from the library app

# URL patterns for the library app
urlpatterns = [
    path('', views.home, name='home'),  # Homepage route
    path('books/', views.book_list, name='book_list'),  # Route for the list of books
    path('books/<int:pk>/', views.book_detail, name='book_detail'),  # Route for book detail page with book id (primary key)
    path('about-us/', views.about_us, name='about_us'),  # Route for the About Us page
    path('contact-us/', views.contact_us, name='contact_us'),  # Route for the Contact Us page
]
