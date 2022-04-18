from django.shortcuts import render, redirect
from books.models import Book


def index(request):
    return redirect('books')


def books_view(request):
    books = Book.objects.all()
    template = 'books/books_list.html'
    context = {'books': books}
    return render(request, template, context)

#  вариант 2
# def books_by_date(request, date):
#     template = 'books/books_list.html'
#     books = Book.objects.filter(pub_date=date)
#     dates = sorted(list(set([book.pub_date.strftime('%Y-%m-%d')
#     for book in Book.objects.all()])))
#     index = dates.index(date)
#     context = {
#         'books': books,
#     }
#     if index == 0:
#         context['previous_date'] = None
#         context['next_date'] = dates[index + 1]
#     elif index == len(dates) - 1:
#         context['next_date'] = None
#         context['previous_date'] = dates[index - 1]
#     else:
#         context['next_date'] = dates[index + 1]
#         context['previous_date'] = dates[index - 1]
#     return render(request, template, context)


def books_by_date(request, date):
    template = 'books/books_list.html'
    books = Book.objects.filter(pub_date=date)
    last_book_index = len(books) - 1
    try:
        previous_date = books[0].get_previous_by_pub_date().\
            pub_date.strftime('%Y-%m-%d')
    except Book.DoesNotExist:
        previous_date = None
    try:
        next_date = books[last_book_index].get_next_by_pub_date().\
            pub_date.strftime('%Y-%m-%d')
    except Book.DoesNotExist:
        next_date = None

    context = {
        'books': books,
        'previous_date': previous_date,
        'next_date': next_date
    }
    return render(request, template, context)
