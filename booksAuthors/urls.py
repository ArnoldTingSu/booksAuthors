from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('authors', views.authors),
    path('add_book', views.add_book),
    path('add_author', views.add_author),
    path('book/<int:book_id>', views.book_details),
    path('authors/<int:author_id>', views.authors_details),
    path('book/assign_author/<int:book_id>', views.assign_author),
    path('authors/assign_book/<int:author_id>', views.assign_book)
    
]