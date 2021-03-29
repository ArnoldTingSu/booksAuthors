from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author

# Create your views here.

def index(request):
    context  = {
        'books': Book.objects.all()
    }
    return render(request, 'add_book.html', context)

def authors(request):
    context = {
        'authors': Author.objects.all() 
    }
    return render(request, 'add_author.html', context)

def add_book(request):
    Book.objects.create(
        title=(request.POST['title']),
        desc=(request.POST['description'])
        )
    return redirect('/')

def add_author(request):
    Author.objects.create(
        name=(request.POST['name']),
        notes=(request.POST['notes'])
    )
    return redirect('/authors')

def book_details(request, book_id):
    context = {
        'books': Book.objects.get(id=book_id),
        'authors': Book.objects.get(id=book_id).authors.all(),
        'other_authors': Author.objects.exclude(books=(Book.objects.get(id=book_id)))   
    }
    return render(request, 'book_details.html', context)

def authors_details(request, author_id):
    context = {
        'authors': Author.objects.get(id=author_id),
        'books': Author.objects.get(id=author_id).books.all(),
        'other_books': Book.objects.exclude(authors=(Author.objects.get(id=author_id)))
    }
    return render(request, 'author_details.html', context)

def assign_author(request, book_id):
    context = {
        'books': Book.objects.all()
    }
    book_addee = Book.objects.get(id=book_id)
    book_addee.authors.add(Author.objects.get(id=(request.POST['author_selection'])))
    url = book_id
    return redirect(f'/book/{url}')


def assign_book(request, author_id):
    context = {
        'authors': Author.objects.all()
    }
    author_addee = Author.objects.get(id=author_id)
    author_addee.books.add(Book.objects.get(id=(request.POST['book_selection'])))
    url=author_id
    return redirect(f'/authors/{url}')


