from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book  
from .forms import BookForm  
from django.contrib import messages


def index(request):
    books = Book.objects.all()
    return render(request, 'main/index.html', {'books': books})

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'main/book_detail.html', {'book': book})


@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)  
            book.user = request.user 
            book.save()  
            return redirect('index')
        else:
           
            return render(request, 'main/add_book.html', {'form': form})
    else:
       
        form = BookForm()
        return render(request, 'main/add_book.html', {'form': form})

@login_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book.user != request.user:
        messages.error(request, "You do not have permission to edit this book.")
        return redirect('index') 

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Book updated successfully.")
            return redirect('index')  
    else:
        form = BookForm(instance=book)

    return render(request, 'main/edit_book.html', {'form': form, 'book': book})

@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book.user != request.user:
        messages.error(request, "You do not have permission to delete this book.")
        return redirect('index')  
    if request.method == 'POST':
        book.delete()
        messages.success(request, "Book deleted successfully.")
        return redirect('index')  

    return render(request, 'main/delete_book.html', {'book': book})
