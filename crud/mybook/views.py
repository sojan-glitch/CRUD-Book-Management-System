
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book


# Create and Read
def book_list(request):
    if request.method == 'POST':
        Book.objects.create(
            title=request.POST.get('title'),
            author=request.POST.get('author'),
            price=request.POST.get('price')
        )
        return redirect('book_list')

    books = Book.objects.all()
    return render(request, 'mybook/book_list.html', {'books': books})


# Update
def update_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.price = request.POST.get('price')
        book.save()
        return redirect('book_list')

    return render(request, 'mybook/update_book.html', {'book': book})


# Delete
def delete_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.delete()

    return redirect('book_list')
